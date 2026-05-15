# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.vga_brand_repository import VgaBrandRepository
from infrastructure.database.models.vga_brand_model import VgaBrandModel


class SqlAlchemyVgaBrandRepository(VgaBrandRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[VgaBrandModel]:
        return self.session.execute(
            select(VgaBrandModel).order_by(VgaBrandModel.id)
        ).scalars().all()
