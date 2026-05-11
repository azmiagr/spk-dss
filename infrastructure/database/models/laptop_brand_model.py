from typing import List

# pyrefly: ignore [missing-import]
from sqlalchemy import Integer, String
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base


class LaptopBrandModel(Base):
    __tablename__ = "laptop_brands"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    laptops: Mapped[List["LaptopModel"]] = relationship("LaptopModel", back_populates="brand")
