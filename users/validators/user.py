from typing import Any

from models import User
from validators.base import BaseValidator, validation_check
from validators.mixins.unique import UniqueMixin
from validators.scenarios import UserScenario


class UserValidator(BaseValidator, UniqueMixin[User]):
    @validation_check(UserScenario.CREATE, UserScenario.UPDATE)
    async def unique_email(self, data: dict[str, Any]):
        await self._check_unique(User, "email", data)

    @validation_check(UserScenario.CREATE, UserScenario.UPDATE)
    async def unique_username(self, data: dict[str, Any]):
        await self._check_unique(User, "username", data)

