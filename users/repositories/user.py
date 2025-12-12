import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from repositories.base import RepositoryBase
from schemas.user import UserCreate, UserUpdate


class UserRepository(RepositoryBase[User, UserCreate, UserUpdate, uuid.UUID]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)
