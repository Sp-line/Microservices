import uuid

from fastapi import UploadFile

from exceptions.model import ObjectNotFound
from repositories.user import UserRepository
from schemas.user import UserRead, UserCreate, UserUpdate
from services.interfaces.image import AImageService
from validators.scenarios import UserScenario
from validators.user import UserValidator


class UserService:
    def __init__(self, repository: UserRepository, validator: UserValidator):
        self.repository = repository
        self.validator = validator

    async def get_all(self) -> list[UserRead]:
        return [UserRead.model_validate(user) for user in await self.repository.get_all()]

    async def get_by_id(self, user_id: uuid.UUID) -> UserRead:
        user = await self.repository.get_by_id(user_id)
        if user is None:
            raise ObjectNotFound(self.repository.model, user_id)
        return UserRead.model_validate(user)

    async def create(self, data: UserCreate) -> UserRead:
        await self.validator.validate(data.model_dump(), UserScenario.CREATE)
        return UserRead.model_validate(await self.repository.create(data))

    async def update(self, user_id: uuid.UUID, data: UserUpdate) -> UserRead:
        await self.validator.validate(data.model_dump(exclude_unset=True), UserScenario.UPDATE)
        return UserRead.model_validate(await self.repository.update(user_id, data))

    async def delete(self, user_id: uuid.UUID) -> None:
        deleted = await self.repository.delete(user_id)
        if not deleted:
            raise ObjectNotFound(self.repository.model, user_id)


class UserAvatarService(AImageService):
    RESIZE_TO = (400, 400)

    def get_folder_name(self, identifier: str) -> str:
        return "avatars"

    def generate_filename(self, file: UploadFile, identifier: str) -> str:
        return "".join(c for c in identifier if c.isalnum() or c in ('-', '_'))
