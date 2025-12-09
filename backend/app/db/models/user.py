from tortoise import fields
import base

class User(base.BaseMixin, base.BaseModel):

    provider: str = fields.CharField(max_length=128, null=True)
    email: str = fields.CharField(max_length=128)
    firstname: str = fields.CharField(max_length=128)
    lastname: str = fields.CharField(max_length=128)
    hashed_password: str = fields.CharField(max_length=128)
    email_verified: bool = fields.BooleanField(default=False)

