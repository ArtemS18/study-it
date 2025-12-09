from typing import Annotated
from fastapi import APIRouter, Form

from backend.app.schemas import auth

auth_router = APIRouter(prefix="/auth")

auth_router.post("/reg")
async def register_handler(user_form: Annotated[auth.RegisterUserForm, Form()]):
    
