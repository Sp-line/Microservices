from uuid import UUID

from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    id: UUID
    email: EmailStr
    username: str
    email_verified: bool


class UserRead(UserBase):
    avatar: str | None = None
    active: bool

    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    avatar: str | None = None
    active: bool = True


class UserUpdate(BaseModel):
    email: EmailStr | None = None
    username: str | None = None
    avatar: str | None = None
    active: bool | None = None
    email_verified: bool | None = None

