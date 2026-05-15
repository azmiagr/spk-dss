# pyrefly: ignore [missing-import]
from flask import Blueprint
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_processors import GetProcessorsUseCase
from helpers.response import http_response
from infrastructure.database.repositories.processor_repository_impl import (
    SqlAlchemyProcessorRepository,
)


def create_processor_blueprint(session_factory):
    processor_blueprint = Blueprint("processor", __name__)

    @processor_blueprint.get("/processors")
    def get_processors():
        session = session_factory()

        try:
            processor_repository = SqlAlchemyProcessorRepository(session)
            get_processors_use_case = GetProcessorsUseCase(processor_repository)

            data = get_processors_use_case.execute()

            return http_response(
                code=200,
                is_success=True,
                message="success to get processors",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get processors",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return processor_blueprint
