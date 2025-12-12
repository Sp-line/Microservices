from sqlalchemy.orm import Mapped

from models import Base
from models.types.pk_type import PK


class PKTypeModel(Base):
    __abstract__ = True

    id: Mapped[PK]
