from typing import List

# pyrefly: ignore [missing-import]
from sqlalchemy import Integer, String
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base

class CriterionModel(Base):
    __tablename__ = "criteria"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    criteria_code: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    attribute_type: Mapped[str] = mapped_column(String(20), nullable=False)
    default_weight: Mapped[int] = mapped_column(Integer, nullable=False)