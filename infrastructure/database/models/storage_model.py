from typing import List

# pyrefly: ignore [missing-import]
from sqlalchemy import Integer, String
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Mapped, mapped_column, relationship

from infrastructure.database.base import Base

class StorageModel(Base):
    __tablename__ = "storages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    storage_type: Mapped[str] = mapped_column(String(50), nullable=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)

    laptop_links: Mapped[List["LaptopStorageModel"]] = relationship("LaptopStorageModel", back_populates="storage")