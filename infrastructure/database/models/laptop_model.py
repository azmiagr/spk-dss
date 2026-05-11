from datetime import datetime
from decimal import Decimal
from typing import List

# pyrefly: ignore [missing-import]
from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String, func
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base

class LaptopModel(Base):
    __tablename__ = "laptops"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    brand_id: Mapped[int] = mapped_column(ForeignKey("laptop_brands.id"), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey("laptop_types.id"), nullable=False)
    os_id: Mapped[int] = mapped_column(ForeignKey("operating_systems.id"), nullable=False)
    processor_id: Mapped[int] = mapped_column(ForeignKey("processors.id"), nullable=False)
    vga_id: Mapped[int] = mapped_column(ForeignKey("vgas.id"), nullable=False)
    display_id: Mapped[int] = mapped_column(ForeignKey("displays.id"), nullable=False)

    ram_capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    ram_type: Mapped[str] = mapped_column(String(50), nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(14, 2), nullable=False)
    weight: Mapped[int] = mapped_column(Integer, nullable=False)
    battery_backup: Mapped[int] = mapped_column(Integer, nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    brand: Mapped["LaptopBrandModel"] = relationship("LaptopBrandModel", back_populates="laptops")
    type: Mapped["LaptopTypeModel"] = relationship("LaptopTypeModel", back_populates="laptops")
    operating_system: Mapped["OperatingSystemModel"] = relationship("OperatingSystemModel", back_populates="laptops")
    processor: Mapped["ProcessorModel"] = relationship("ProcessorModel", back_populates="laptops")
    vga: Mapped["VgaModel"] = relationship("VgaModel", back_populates="laptops")
    display: Mapped["DisplayModel"] = relationship("DisplayModel", back_populates="laptops")
    storage_links: Mapped[List["LaptopStorageModel"]] = relationship("LaptopStorageModel", back_populates="laptop")
