from typing import TypeVar

from models.mixins.pk_type import PKTypeModel

ModelType = TypeVar("ModelType", bound=PKTypeModel)
