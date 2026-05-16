# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.vga_repository import VgaRepository
from infrastructure.database.models.vga_model import VgaModel


class SqlAlchemyVgaRepository(VgaRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[VgaModel]:
        return self.session.execute(
            select(VgaModel).order_by(VgaModel.id)
        ).scalars().all()
