from uuid import UUID

from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    id: UUID
    email: EmailStr
    username: str


class UserRead(UserBase):
    avatar: str | None = None
    active: bool

    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    avatar: str | None = None
    active: bool = True


class UserUpdate(BaseModel):
    username: str | None = None

