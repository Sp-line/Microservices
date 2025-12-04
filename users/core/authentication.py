from fastapi.security import OAuth2AuthorizationCodeBearer
from fief_client import FiefAsync
from fief_client.integrations.fastapi import FiefAuth

from core.config import settings

fief = FiefAsync(
    settings.fief.url,
    settings.fief.client_id,
    settings.fief.client_secret,
)

scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{settings.fief.url}/authorize",
    tokenUrl=f"{settings.fief.url}/api/token",
    scopes={"openid": "openid", "email": "email", "profile": "profile"},
)

auth = FiefAuth(fief, scheme)
