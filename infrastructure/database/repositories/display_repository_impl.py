# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.display_repository import DisplayRepository
from infrastructure.database.models.display_model import DisplayModel


class SqlAlchemyDisplayRepository(DisplayRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[DisplayModel]:
        return self.session.execute(
            select(DisplayModel).order_by(DisplayModel.id)
        ).scalars().all()
