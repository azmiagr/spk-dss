# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.operating_system_repository import OperatingSystemRepository
from infrastructure.database.models.operating_system_model import OperatingSystemModel


class SqlAlchemyOperatingSystemRepository(OperatingSystemRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[OperatingSystemModel]:
        return self.session.execute(
            select(OperatingSystemModel).order_by(OperatingSystemModel.id)
        ).scalars().all()
