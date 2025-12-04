from sqlalchemy.orm import Mapped

from core.models import Base
from core.models.types.pk_type import PK


class PKTypeModel(Base):
    __abstract__ = True

    id: Mapped[PK]
