from typing import Type, TypeVar
from tortoise import models
from tortoise.contrib.pydantic import PydanticModel
from pydantic import BaseModel

_TortoiseModel = TypeVar("TortoiseModel", bound=models.Model)
_GetSchema = TypeVar("GetSchema", bound=PydanticModel)
_UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)
_CreateSchema = TypeVar("CreateSchema", bound=BaseModel)


class BaseService():
    model: Type[_TortoiseModel]
    create_schema: Type[_CreateSchema]
    update_schema: Type[_UpdateSchema]
    get_schema: Type[_GetSchema]

    async def create(self, _create_schema: Type[_CreateSchema]) -> Type[_GetSchema]:
        obj = await self.model.create(**_create_schema.model_dump(exclude_unset=True))
        return await self.get_schema.from_tortoise_orm(obj)
    
    async def get_s(self, **kwargs) -> Type[_GetSchema]:
        return await self.get_schema.from_queryset_single(self.model.filter(**kwargs).first())
    
    async def update(self, _update_schema:Type[_UpdateSchema],  **kwargs):
        obj = await self.model.filter(**kwargs).update(**_update_schema.model_dump(exclude_unset=True))

        return await self.get_schema.from_tortoise_orm(obj)
    
    async def all(self, **kwargs) -> Type[_GetSchema]:
        return await self.get_schema.from_queryset(self.model.filter(**kwargs).all())
    
    async def delete(self, **kwargs) -> Type[_GetSchema]:
        obj = await self.get_s(**kwargs)
        await self.model.delete(**kwargs)
        return obj