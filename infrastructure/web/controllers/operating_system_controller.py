# pyrefly: ignore [missing-import]
from flask import Blueprint
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_operating_systems import GetOperatingSystemsUseCase
from helpers.response import http_response
from infrastructure.database.repositories.operating_system_repository_impl import (
    SqlAlchemyOperatingSystemRepository,
)


def create_operating_system_blueprint(session_factory):
    operating_system_blueprint = Blueprint("operating_system", __name__)

    @operating_system_blueprint.get("/operating-systems")
    def get_operating_systems():
        session = session_factory()

        try:
            operating_system_repository = SqlAlchemyOperatingSystemRepository(session)
            get_operating_systems_use_case = GetOperatingSystemsUseCase(
                operating_system_repository
            )

            data = get_operating_systems_use_case.execute()

            return http_response(
                code=200,
                is_success=True,
                message="success to get operating systems",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get operating systems",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return operating_system_blueprint
