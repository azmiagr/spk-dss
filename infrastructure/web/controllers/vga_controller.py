# pyrefly: ignore [missing-import]
from flask import Blueprint
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_vgas import GetVgasUseCase
from helpers.response import http_response
from infrastructure.database.repositories.vga_repository_impl import (
    SqlAlchemyVgaRepository,
)


def create_vga_blueprint(session_factory):
    vga_blueprint = Blueprint("vga", __name__)

    @vga_blueprint.get("/vgas")
    def get_vgas():
        session = session_factory()

        try:
            vga_repository = SqlAlchemyVgaRepository(session)
            get_vgas_use_case = GetVgasUseCase(vga_repository)

            data = get_vgas_use_case.execute()

            return http_response(
                code=200,
                is_success=True,
                message="success to get vgas",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get vgas",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return vga_blueprint
