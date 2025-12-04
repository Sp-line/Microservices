from typing import Generic, TypeVar, Type, Sequence

from pydantic import BaseModel
from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from core.models.mixins.pk_type import PKTypeModel
from core.models.types.pk_type import PK

PKType = TypeVar('PKType', bound=PK)

ModelType = TypeVar("ModelType", bound=PKTypeModel)

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class RepositoryBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType, PKType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def get_all(self) -> Sequence[ModelType]:
        stmt = select(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_by_id(self, obj_id: PKType) -> ModelType | None:
        return await self.session.get(self.model, obj_id)

    async def create(self, data: CreateSchemaType) -> ModelType:
        obj = self.model(**data.model_dump())
        self.session.add(obj)
        await self.session.commit()
        await self.session.refresh(obj)
        return obj

    async def update(self, obj_id: PKType, data: UpdateSchemaType) -> ModelType | None:
        stmt = (
            update(self.model)
            .where(self.model.id == obj_id)
            .values(data.model_dump(exclude_unset=True))
            .returning(self.model)
        )
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.scalar_one_or_none()

    async def delete(self, obj_id: PKType) -> bool:
        obj = await self.get_by_id(obj_id)
        if not obj:
            return False

        await self.session.delete(obj)
        await self.session.commit()
        return True
