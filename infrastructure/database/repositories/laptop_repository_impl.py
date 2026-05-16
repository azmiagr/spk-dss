# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.laptop_repository import LaptopRepository
from infrastructure.database.models.laptop_model import LaptopModel


class SqlAlchemyLaptopRepository(LaptopRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[LaptopModel]:
        return self.session.execute(
            select(LaptopModel).order_by(LaptopModel.id)
        ).scalars().all()
