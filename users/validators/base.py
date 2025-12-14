import inspect
from enum import Enum
from typing import Any, Annotated

from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import db


def validation_check(*scenarios: Enum):
    def decorator(func):
        func._is_validation_check = True
        func._validation_scenarios = set(scenarios)
        return func

    return decorator


class BaseValidator:
    session: AsyncSession

    def __init__(self, session: Annotated[AsyncSession, Depends(db.session)]) -> None:
        self.session = session

    async def validate(self, data: dict[str, Any], scenario: Enum = None) -> None:
        for attr_name in dir(self):
            if attr_name.startswith("__"): continue

            method = getattr(self, attr_name)

            if callable(method) and getattr(method, "_is_validation_check", False):
                method_scenarios: set[Enum] = getattr(method, "_validation_scenarios", set())

                should_run = (scenario is None) or (scenario in method_scenarios)
                if should_run:
                    if inspect.iscoroutinefunction(method):
                        await method(data)
                    else:
                        method(data)
