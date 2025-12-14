from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from models import db


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup логіка
    yield
    # shutdown логіка
    await db.dispose()


main_app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
