import uuid

from sqlalchemy import String, Boolean, Uuid
from sqlalchemy.orm import Mapped, mapped_column

from models.mixins.pk_type import PKTypeModel


class User(PKTypeModel):
    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, index=True)

    username: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    avatar: Mapped[str] = mapped_column(String, nullable=True)

    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    def __repr__(self):
        return f"<User(fief_id={self.id}, email={self.email})>"
