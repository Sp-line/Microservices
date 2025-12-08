from fastapi import APIRouter

from api.api_v1.webhooks import webhooks_router
from core.config import settings

router = APIRouter(
    prefix=settings.api.v1.prefix,
)

router.include_router(webhooks_router)
