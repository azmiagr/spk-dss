# pyrefly: ignore [missing-import]
from flask import Blueprint
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_laptop_types import GetLaptopTypesUseCase
from helpers.response import http_response
from infrastructure.database.repositories.laptop_type_repository_impl import (
    SqlAlchemyLaptopTypeRepository,
)


def create_laptop_type_blueprint(session_factory):
    laptop_type_blueprint = Blueprint("laptop_type", __name__)

    @laptop_type_blueprint.get("/laptop-types")
    def get_laptop_types():
        session = session_factory()

        try:
            laptop_type_repository = SqlAlchemyLaptopTypeRepository(session)
            get_laptop_types_use_case = GetLaptopTypesUseCase(laptop_type_repository)

            data = get_laptop_types_use_case.execute()

            return http_response(
                code=200,
                is_success=True,
                message="success to get laptop types",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get laptop types",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return laptop_type_blueprint
