# pyrefly: ignore [missing-import]
from sqlalchemy import func, select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.laptop_repository import LaptopRepository
from infrastructure.database.models.display_model import DisplayModel
from infrastructure.database.models.laptop_model import LaptopModel
from infrastructure.database.models.laptop_storage_model import LaptopStorageModel
from infrastructure.database.models.storage_model import StorageModel


class SqlAlchemyLaptopRepository(LaptopRepository):
    def __init__(self, session: Session):
        self.session = session

    def _apply_filters(self, stmt, filters: dict):
        if not filters:
            return stmt

        if filters.get("max_price") is not None:
            stmt = stmt.where(LaptopModel.price <= filters["max_price"])
        if filters.get("brand_id") is not None:
            stmt = stmt.where(LaptopModel.brand_id == filters["brand_id"])
        if filters.get("os_id") is not None:
            stmt = stmt.where(LaptopModel.os_id == filters["os_id"])
        if filters.get("type_id") is not None:
            stmt = stmt.where(LaptopModel.type_id == filters["type_id"])
        if filters.get("display_size") is not None:
            stmt = stmt.join(DisplayModel, LaptopModel.display_id == DisplayModel.id)
            stmt = stmt.where(DisplayModel.size == filters["display_size"])
        if filters.get("min_ram") is not None:
            stmt = stmt.where(LaptopModel.ram_capacity >= filters["min_ram"])
        if filters.get("min_storage") is not None:
            stmt = (
                stmt
                .join(LaptopStorageModel, LaptopModel.id == LaptopStorageModel.laptop_id)
                .join(StorageModel, LaptopStorageModel.storage_id == StorageModel.id)
                .where(StorageModel.capacity >= filters["min_storage"])
            )

        return stmt

    def get_all(self, page: int, per_page: int, filters: dict = None) -> list[LaptopModel]:
        offset = (page - 1) * per_page
        stmt = select(LaptopModel).distinct()
        stmt = self._apply_filters(stmt, filters)
        stmt = stmt.order_by(LaptopModel.id).limit(per_page).offset(offset)
        return self.session.execute(stmt).scalars().all()

    def count(self, filters: dict = None) -> int:
        inner = select(LaptopModel.id).distinct()
        inner = self._apply_filters(inner, filters)
        stmt = select(func.count()).select_from(inner.subquery())
        return self.session.execute(stmt).scalar()

    def get_all_for_dss(self, filters: dict = None) -> list[LaptopModel]:
        stmt = select(LaptopModel).distinct()
        stmt = self._apply_filters(stmt, filters)
        stmt = stmt.order_by(LaptopModel.id)
        return self.session.execute(stmt).scalars().all()
