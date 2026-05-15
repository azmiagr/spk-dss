# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.laptop_brand_repository import LaptopBrandRepository
from infrastructure.database.models.laptop_brand_model import LaptopBrandModel


class SqlAlchemyLaptopBrandRepository(LaptopBrandRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[LaptopBrandModel]:
        return self.session.execute(
            select(LaptopBrandModel).order_by(LaptopBrandModel.id)
        ).scalars().all()
