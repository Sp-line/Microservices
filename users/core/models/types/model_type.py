from typing import TypeVar

from core.models.mixins.pk_type import PKTypeModel

ModelType = TypeVar("ModelType", bound=PKTypeModel)
