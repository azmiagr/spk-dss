# pyrefly: ignore [missing-import]
from flask import Blueprint
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_displays import GetDisplaysUseCase
from helpers.response import http_response
from infrastructure.database.repositories.display_repository_impl import (
    SqlAlchemyDisplayRepository,
)


def create_display_blueprint(session_factory):
    display_blueprint = Blueprint("display", __name__)

    @display_blueprint.get("/displays")
    def get_displays():
        session = session_factory()

        try:
            display_repository = SqlAlchemyDisplayRepository(session)
            get_displays_use_case = GetDisplaysUseCase(display_repository)

            data = get_displays_use_case.execute()

            return http_response(
                code=200,
                is_success=True,
                message="success to get displays",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get displays",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return display_blueprint
