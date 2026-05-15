# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session

from domain.repositories.storage_repository import StorageRepository
from infrastructure.database.models.storage_model import StorageModel


class SqlAlchemyStorageRepository(StorageRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[StorageModel]:
        return self.session.execute(
            select(StorageModel).order_by(StorageModel.id)
        ).scalars().all()
