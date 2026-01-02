from fastapi import APIRouter, Depends
from app.depends import get_current_user_id
from schemas import skill_schema
from service import progress


user_router = APIRouter(prefix="/user")


@user_router.post("/roadmap", response_model=skill_schema.ModulePath)
async def create_user_path(
    schema: skill_schema.ModulesIn, user_id: int = Depends(get_current_user_id)
):
    return await progress.create_user_path(user_id, schema.target_modules)


@user_router.get("/roadmap", response_model=skill_schema.ModulePath)
async def get_user_path(user_id: int = Depends(get_current_user_id)):
    return await progress.get_current_user_path(user_id)
