# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.cpu_brand_repository import CpuBrandRepository
from infrastructure.database.models.cpu_brand_model import CpuBrandModel


class SqlAlchemyCpuBrandRepository(CpuBrandRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[CpuBrandModel]:
        return self.session.execute(
            select(CpuBrandModel).order_by(CpuBrandModel.id)
        ).scalars().all()
