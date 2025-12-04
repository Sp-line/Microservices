from datetime import datetime
from enum import Enum
from typing import Any
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


class FiefEventType(str, Enum):
    USER_CREATED = "user.created"
    USER_UPDATED = "user.updated"
    USER_DELETED = "user.deleted"


class FiefTenant(BaseModel):
    id: UUID
    name: str
    slug: str
    default: bool
    registration_allowed: bool
    created_at: datetime
    updated_at: datetime

    application_url: str | None = None
    logo_url: str | None = None
    theme_id: str | None = None


class FiefUser(BaseModel):
    id: UUID
    email: EmailStr
    email_verified: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime

    tenant_id: UUID
    tenant: FiefTenant

    fields: dict[str, Any] = Field(default_factory=dict)


class FiefWebhookPayload(BaseModel):
    type: FiefEventType
    data: FiefUser
