import asyncio
from schemas.skill_schema import ModuleOut, ModulePath, SkillOut
from schemas.graph_schema import GraphGet, NodeGet, EdgeGet
from neomodel import adb
from neo4j.graph import Node, Relationship
from neo4j_client import models

from service import roadmap


async def get_graph_by_topic(topic: str) -> GraphGet:
    cypq = (
        "MATCH (:Subject{code: $topic_code})-[:LEARN]->(root:Module)"
        "MATCH (root)-[n:REQUIRES*0..]->(m:Module)"
        "OPTIONAL MATCH (m)-[inc:INCLUDE*]->(s:Skill) "
        "RETURN collect(DISTINCT m) AS modules, collect(DISTINCT s) AS skills, collect(DISTINCT n) as nextRelations, collect(DISTINCT inc) AS includeRelations;"
    )
    raw, _ = await adb.cypher_query(cypq, {"topic_code": topic})
    row: tuple[
        list[Node],
        list[Node],
        list[tuple[Relationship, ...]],
        list[tuple[Relationship, ...]],
    ] = raw[0]
    modules, skills, next_rel, inc_rel = row

    modules_nd = [NodeGet.from_neo4j(m) for m in modules]
    skills_nd = [NodeGet.from_neo4j(m) for m in skills]
    next_edg = [EdgeGet.from_neo4j(m) for m in next_rel if m != []]
    inc_edg = [EdgeGet.from_neo4j(m) for m in inc_rel if m != []]

    return GraphGet(nodes=modules_nd + skills_nd, edges=next_edg + inc_edg)


async def get_next_modules(id: str) -> ModulePath:
    cypq = (
        "MATCH (prev:Module)-[:REQUIRES]->(next:Module) "
        "WHERE prev.code = $id "
        "OPTIONAL MATCH (next)-[:INCLUDE]->(skill:Skill) "
        "RETURN next, collect(DISTINCT skill) AS skills "
        "ORDER BY next.code;"
    )
    raw, _ = await adb.cypher_query(cypq, {"id": id})
    roadmap = []
    for row in raw:
        m: Node = row[0]
        skills: list[Node] = row[1]
        roadmap.append(
            ModuleOut(
                id=m._properties.get("code"),
                name=m._properties.get("name"),
                skills=[
                    SkillOut(
                        id=s._properties.get("code"), name=s._properties.get("name")
                    )
                    for s in skills
                ],
            )
        )
    return ModulePath(path=roadmap)


async def get_path_beetwen_modules(from_id: str, to_id: str) -> ModulePath:
    await roadmap.get_roadmap([from_id], [to_id])
