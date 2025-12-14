import uuid
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import User, db
from repositories.base import RepositoryBase
from schemas.user import UserCreate, UserUpdate


class UserRepository(RepositoryBase[User, UserCreate, UserUpdate, uuid.UUID]):
    def __init__(self, session: Annotated[AsyncSession, Depends(db.session)] ) -> None:
        super().__init__(User, session)
