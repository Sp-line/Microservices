from fastapi import Request
from fastapi.responses import JSONResponse

from core.server import main_app
from exceptions.model import ObjectNotFound, ModelUniqueField


@main_app.exception_handler(ObjectNotFound)
async def object_not_found_handler(request: Request, exc: ObjectNotFound) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={
            "error_code": f"{exc.model.__name__.upper()}_NOT_FOUND",
            "detail": exc.message,
            "user_id": str(exc.obj_id),
            "model": exc.model.__name__,
        }
    )


@main_app.exception_handler(ModelUniqueField)
async def model_unique_field_handler(request: Request, exc: ModelUniqueField) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={
            "error_code": f"{exc.model.__name__.upper()}_ALREADY_EXISTS",
            "detail": exc.message,
            "model": exc.model.__name__,
            "field": exc.field,
            "value": exc.value,
        }
    )
