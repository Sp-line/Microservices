import os

import uvicorn
from fastapi.staticfiles import StaticFiles

import exceptions.handlers  # noqa
from api import router as api_router
from core.config import settings
from core.server import main_app

main_app.include_router(
    api_router,
)

os.makedirs("static/avatars", exist_ok=True)
main_app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
