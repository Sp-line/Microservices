import uvicorn

import exceptions.handlers  # noqa
from api import router as api_router
from core.config import settings
from core.server import main_app

main_app.include_router(
    api_router,
)

if __name__ == "__main__":
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
