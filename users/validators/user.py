from typing import Any

from models import User
from validators.base import BaseValidator, validation_check
from validators.mixins.existence import ExistenceMixin
from validators.mixins.unique import UniqueMixin
from validators.scenarios import UserScenario


class UserValidator(BaseValidator, UniqueMixin[User], ExistenceMixin[User]):
    @validation_check(UserScenario.CREATE, UserScenario.UPDATE)
    async def unique_email(self, data: dict[str, Any]):
        await self._check_unique(User, "email", data)

    @validation_check(UserScenario.CREATE, UserScenario.UPDATE)
    async def unique_username(self, data: dict[str, Any]):
        await self._check_unique(User, "username", data)

    @validation_check(UserScenario.UPDATE, UserScenario.DELETE, UserScenario.GET_BY_ID)
    async def user_exists(self, data: dict[str, Any]):
        await self._ensure_exists(User, data["id"])