from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "userpath" ADD "path_hash" VARCHAR(257) NOT NULL;
        ALTER TABLE "userpath" ALTER COLUMN "current_module_code" DROP NOT NULL;
        CREATE INDEX IF NOT EXISTS "idx_userpath_path_ha_99cf82" ON "userpath" ("path_hash");"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP INDEX IF EXISTS "idx_userpath_path_ha_99cf82";
        ALTER TABLE "userpath" DROP COLUMN "path_hash";
        ALTER TABLE "userpath" ALTER COLUMN "current_module_code" SET NOT NULL;"""


MODELS_STATE = (
    "eJztWttu2zgQ/RVDTynQLRrl4qBvsuNsvbXjIHZ2iwaBQEu0TESiVIlKbAT595LU/VrLaz"
    "V2yydbwxmKPCRn5oz4InnQfYLuBwW6SFtKnzovEgYWpH9yLe87EnCcRM4EBMxNrgoSnblH"
    "XKARKl0A04NUpENPc5FDkI2pFPumyYS2RhURNhKRj9F3H6rENiBZ0hd86tw/UDHCOlxBL3"
    "p0HtUFgqaeGSrS2bu5XCVrh8uGmFxxRfa2uarZpm/hRNlZk6WNY22ECZMaEEMXEMi6J67P"
    "hs9GF84zmlEw0kQlGGLKRocL4JskNd0NMdBszPCjo/H4BA32lr/k49Pu6cXJ+ekFVeEjiS"
    "Xd12B6ydwDQ47A9Ux65e2AgECDw5jgRtfRY0MqgNdfArccvZRJDkI68DyEEWB1GEaCBMRk"
    "4+wIRQusVBNig7ANLp+d1WD2r3Lb/6zcHlGtd2w2Nt3MwR6/DpvkoI0BmwDJjkYDEEP1ww"
    "Tw+OPHDQCkWpUA8rYsgPSNBAZnMAviP9PJdTmIKZMckHeYTvBeRxp53zGRRx72E9YaFNms"
    "2aAtz/tupsE7Gitf87j2R5MeR8H2iOHyXngHPYoxc5mLx9ThZ4I50B6fgaurhRZbtqt0i0"
    "2WbOUlAAODY8VmzOYXBpEpAcT3ysJL2FIbXrxEZ2/Cy9QCpvkbxZgTuXsehxf2UBdZpmNl"
    "NPp5eOG/DdxipH+YfvFE3sAtnsiVXpE1NTqwCdA+PTSqZeu+CVXHtZkT8Lwi8r2wm6svt9"
    "AEpCKMB+fyjv6OeY83YYf7uQav0SaKpOEJyUQXho8DyHIHmNzQbg4MiTYdO4OkzK1zea1T"
    "9yONvXHpv5E3b40xaC5kk1VBSap2SVsIsmBFupaxzIGph6Yfoj8bHLEQuV/p7+kU9Ak214"
    "mPqUJyNhwPpjNlfJPJ4i6V2YC1yFy6zkmPznOxIe6k899w9rnDHjvfJteDfLIX682+SWxM"
    "wCe2iu1nFeipLRZJI2CyHtLRt1zXrKVY17dc10Lgo8nAE9IDR7tpFpa22SoTe4MFzBJU+W"
    "ITgipfVBNU1pYlqNACyGwCY2ywm2y29cDRPoQL5HqkKSfIGB0mMWgFTBM0xzJtI6CMoVwC"
    "b0kDmAM879l2SxLDakRLTAWwWZ+p0sQf0U5LcO3ZtgkBrvGfGeMcsnNq3Ra0TZnI5pW93m"
    "QyyuQOveEsB+nduDegWHOkqRIiATsJc/P0vn2CKmVOiP44IS1tAHCZuYB4ywpMUHwRNZdU"
    "6inqLS3VW3JbpKL6UtxI9bWYfP1w97WZ+7jmE75Ks3UoPYiSjSjZCGovSjZ/5roW4mbaNx"
    "bWtZqJ5MzaYiGHV3UIPh6rzb/hZgx/Hkl2lZQc/+9Isv2n3NwXxUYRN2Xx68B6+8hbYAtZ"
    "DIsAXtkuRAb+AtccxyEdEcBa6aHNfkrbP/yqMmAqdsFznMKltwadng5NGPCtvjLtK5cDqe"
    "S87gC35GbJnh3TTWHLOKAMcNPBrHM5uFLuRnQLvs2NnpibVdCPiLfVk46o7tDqR+AXKZkT"
    "p6USU4Arh9Ec2n082YRprFS+Z5myaiBOUaPd9feQ38yCKzpg9hwsgGAsgrGIzFYwlj9gXU"
    "srfcUFrb64W1FsFrd241u7eXRV9p2p0Tf8tNFBckH5rC6GJNf0uzXX9LuFW+a+60JM1C05"
    "doV5S5ckBNUWVFtQbUG1BdVuH7Y9pNqvPwBIxJJn"
)
