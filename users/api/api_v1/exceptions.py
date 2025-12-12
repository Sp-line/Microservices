from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions.model import ObjectNotFound, ModelUniqueField


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


def init_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(ObjectNotFound, object_not_found_handler)
    app.add_exception_handler(ModelUniqueField, model_unique_field_handler)