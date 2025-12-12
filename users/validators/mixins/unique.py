from typing import Type, Generic, Any

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import InstrumentedAttribute

from exceptions.model import ModelUniqueField
from models.types.model_type import ModelType


class UniqueMixin(Generic[ModelType]):
    session: AsyncSession

    async def _check_unique(
            self,
            model: Type[ModelType],
            field_name: str,
            data: dict[str, Any],
    ) -> None:
        if field_name not in data:
            return
        value = data[field_name]

        column: InstrumentedAttribute = getattr(model, field_name)
        stmt = select(model).where(column == value)
        result = await self.session.execute(stmt)

        if result.scalars().first():
            raise ModelUniqueField(model=model.__name__, field=field_name, value=value)
