from pydantic import BaseModel


class RegisterUserForm(BaseModel):
    email: str
    password: str