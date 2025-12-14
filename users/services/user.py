import uuid
from typing import Annotated

from fastapi.params import Depends

from repositories.user import UserRepository
from schemas.user import UserRead, UserCreate, UserUpdate
from validators.scenarios import UserScenario
from validators.user import UserValidator


class UserService:
    def __init__(self,
                 repository: Annotated[UserRepository, Depends(UserRepository)],
                 validator: Annotated[UserValidator, Depends(UserValidator)],
                 ):
        self.repository = repository
        self.validator = validator

    async def get_all(self) -> list[UserRead]:
        return [UserRead.model_validate(user) for user in await self.repository.get_all()]

    async def get_by_id(self, user_id: uuid.UUID) -> UserRead:
        await self.validator.validate({"id": user_id}, UserScenario.GET_BY_ID)
        return UserRead.model_validate(self.repository.get_by_id(user_id))

    async def create(self, data: UserCreate) -> UserRead:
        await self.validator.validate(data.model_dump(), UserScenario.CREATE)
        return UserRead.model_validate(await self.repository.create(data))

    async def update(self, user_id: uuid.UUID, data: UserUpdate) -> UserRead:
        validation_payload = data.model_dump(exclude_unset=True)
        validation_payload["id"] = user_id
        await self.validator.validate(validation_payload, UserScenario.UPDATE)
        return UserRead.model_validate(await self.repository.update(user_id, data))

    async def delete(self, user_id: uuid.UUID) -> None:
        await self.validator.validate({"id": user_id}, UserScenario.DELETE)
        await self.repository.delete(user_id)
