# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.laptop_type_repository import LaptopTypeRepository
from infrastructure.database.models.laptop_type_model import LaptopTypeModel


class SqlAlchemyLaptopTypeRepository(LaptopTypeRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[LaptopTypeModel]:
        return self.session.execute(
            select(LaptopTypeModel).order_by(LaptopTypeModel.id)
        ).scalars().all()
