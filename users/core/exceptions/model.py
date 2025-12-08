from typing import Any

from core.models.mixins.pk_type import PKTypeModel
from core.models.types.pk_type import PK


class ModelUniqueField(Exception):
    def __init__(self, model: str, field: str, value: Any) -> None:
        self.model = model
        self.field = field
        self.value = value
        self.message = f"Object {model.lower()} with field {field}={str(value)} already exists"
        super().__init__(self.message)


class ObjectNotFound(Exception):
    def __init__(self, model: PKTypeModel, obj_id: PK) -> None:
        self.obj_id = obj_id
        self.model = model
        self.message = f"{model.__name__} with id={obj_id} not found"
        super().__init__(self.message)