from typing import List

# pyrefly: ignore [missing-import]
from sqlalchemy import ForeignKey, Integer, String
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base

class VgaModel(Base):
    __tablename__ = "vgas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    brand_id: Mapped[int] = mapped_column(ForeignKey("vga_brands.id"), nullable=False)
    gpu_benchmark_score: Mapped[int] = mapped_column(Integer, nullable=False)
    memory_capacity: Mapped[int] = mapped_column(Integer, nullable=False)

    brand: Mapped["VgaBrandModel"] = relationship("VgaBrandModel", back_populates="vgas")
    laptops: Mapped[List["LaptopModel"]] = relationship("LaptopModel", back_populates="vga")
