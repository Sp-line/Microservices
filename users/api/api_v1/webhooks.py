from typing import Annotated

from fastapi import APIRouter, Depends

from core.config import settings
from dependencies.security import VerifyFiefSignature
from schemas.fief import FiefWebhookPayload
from schemas.user import UserCreate, UserUpdate
from services.user import UserService

webhooks_router = APIRouter(prefix="/webhooks", tags=["Webhooks"])


@webhooks_router.post(
    "/users/created/",
    dependencies=[Depends(VerifyFiefSignature(settings.fief.webhook.created_secret))],
)
async def fief_webhook_users_created(
        payload: FiefWebhookPayload,
        service: Annotated[UserService, Depends(UserService)],
):
    await service.create(
        UserCreate(
            id=payload.data.id,
            email=payload.data.email,
            username=str(payload.data.email).split("@")[0],
            avatar=None,
            active=payload.data.is_active,
        )
    )


@webhooks_router.post(
    "/users/updated/",
    dependencies=[Depends(VerifyFiefSignature(settings.fief.webhook.updated_secret))],
)
async def fief_webhook_users_updated(
        payload: FiefWebhookPayload,
        service: Annotated[UserService, Depends(UserService)]
):
    await service.update(
        payload.data.id,
        UserUpdate(
            email=payload.data.email,
            active=payload.data.is_active,
        )
    )


@webhooks_router.post(
    "/users/deleted/",
    dependencies=[Depends(VerifyFiefSignature(settings.fief.webhook.deleted_secret))],
)
async def fief_webhook_users_deleted(
        payload: FiefWebhookPayload,
        service: Annotated[UserService, Depends(UserService)]
):
    await service.delete(payload.data.id)
