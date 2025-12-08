from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db
from core.repositories.user import UserRepository
from core.services.user import UserService
from core.validators.user import UserValidator


async def get_user_repository(
        session: Annotated[AsyncSession, Depends(db.session)],
) -> UserRepository:
    return UserRepository(session)


async def get_user_validator(
        session: Annotated[AsyncSession, Depends(db.session)]
) -> UserValidator:
    return UserValidator(session)


async def get_user_service(
        repository: Annotated[UserRepository, Depends(get_user_repository)],
        validator: Annotated[UserValidator, Depends(get_user_validator)]
) -> UserService:
    return UserService(repository, validator)
