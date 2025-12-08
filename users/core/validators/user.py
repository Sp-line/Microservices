from typing import Any

from core.models import User
from core.validators.base import BaseValidator, validation_check
from core.validators.mixins.unique import UniqueMixin
from core.validators.scenarios import UserScenario


class UserValidator(BaseValidator, UniqueMixin[User]):
    @validation_check(UserScenario.CREATE, UserScenario.UPDATE)
    async def unique_email(self, data: dict[str, Any]):
        await self._check_unique(User, "email", data)

    @validation_check(UserScenario.CREATE, UserScenario.UPDATE)
    async def unique_username(self, data: dict[str, Any]):
        await self._check_unique(User, "username", data)

