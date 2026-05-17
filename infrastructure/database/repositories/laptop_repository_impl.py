# pyrefly: ignore [missing-import]
from sqlalchemy import func, select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.laptop_repository import LaptopRepository
from infrastructure.database.models.laptop_model import LaptopModel


class SqlAlchemyLaptopRepository(LaptopRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self, page: int, per_page: int) -> list[LaptopModel]:
        offset = (page - 1) * per_page
        return self.session.execute(
            select(LaptopModel).order_by(LaptopModel.id).limit(per_page).offset(offset)
        ).scalars().all()

    def count(self) -> int:
        return self.session.execute(
            select(func.count()).select_from(LaptopModel)
        ).scalar()
