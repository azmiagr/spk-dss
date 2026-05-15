# pyrefly: ignore [missing-import]
from sqlalchemy import select
# pyrefly: ignore [missing-import]
from sqlalchemy.orm import Session, joinedload

from domain.repositories.processor_repository import ProcessorRepository
from infrastructure.database.models.processor_model import ProcessorModel

class SqlAlchemyProcessorRepository(ProcessorRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_all(self) -> list[ProcessorModel]:
        return self.session.execute(
            select(ProcessorModel)
            .options(joinedload(ProcessorModel.brand))
            .order_by(ProcessorModel.id)
        ).scalars().all()