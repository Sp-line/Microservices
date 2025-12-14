from typing import Generic, Type

from sqlalchemy.ext.asyncio import AsyncSession

from exceptions.model import ObjectNotFound
from models.types.model_type import ModelType
from models.types.pk_type import PK


class ExistenceMixin(Generic[ModelType]):
    session: AsyncSession

    async def _ensure_exists(
            self,
            model: Type[ModelType],
            obj_id: PK,
    ) -> None:
        obj = await self.session.get(model, obj_id)

        if not obj:
            raise ObjectNotFound(model=model, obj_id=obj_id)
