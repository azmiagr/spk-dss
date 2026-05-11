from typing import List

# pyrefly: ignore [missing-import]
from sqlalchemy import ForeignKey, Integer, String
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base


class ProcessorModel(Base):
    __tablename__ = "processors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    brand_id: Mapped[int] = mapped_column(ForeignKey("cpu_brands.id"), nullable=False)
    cpu_ranking_score: Mapped[int] = mapped_column(Integer, nullable=False)

    brand: Mapped["CpuBrandModel"] = relationship("CpuBrandModel", back_populates="processors")
    laptops: Mapped[List["LaptopModel"]] = relationship("LaptopModel", back_populates="processor")
