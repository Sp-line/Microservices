import uuid

from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.repositories.base import RepositoryBase
from core.schemas.user import UserCreate, UserUpdate


class UserRepository(RepositoryBase[User, UserCreate, UserUpdate, uuid.UUID]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)
