# pyrefly: ignore [missing-import]
from sqlalchemy import ForeignKey
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base


class LaptopStorageModel(Base):
    __tablename__ = "laptop_storages"

    laptop_id: Mapped[int] = mapped_column(ForeignKey("laptops.id"), primary_key=True)
    storage_id: Mapped[int] = mapped_column(ForeignKey("storages.id"), primary_key=True)

    laptop: Mapped["LaptopModel"] = relationship("LaptopModel", back_populates="storage_links")
    storage: Mapped["StorageModel"] = relationship("StorageModel", back_populates="laptop_links")
