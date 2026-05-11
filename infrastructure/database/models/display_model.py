from typing import List

# pyrefly: ignore [missing-import]
from sqlalchemy import Integer, String
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base

class DisplayModel(Base):
    __tablename__ = "displays"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    size: Mapped[int] = mapped_column(Integer, nullable=False)
    resolution: Mapped[str] = mapped_column(String(50), nullable=False)
    refresh_rate: Mapped[int] = mapped_column(Integer, nullable=False)

    laptops: Mapped[List["LaptopModel"]] = relationship("LaptopModel", back_populates="display")