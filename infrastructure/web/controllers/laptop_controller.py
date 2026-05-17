# pyrefly: ignore [missing-import]
from flask import Blueprint, request
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_laptops import GetLaptopsUseCase
from helpers.response import http_response
from infrastructure.database.repositories.laptop_repository_impl import (
    SqlAlchemyLaptopRepository,
)


def create_laptop_blueprint(session_factory):
    laptop_blueprint = Blueprint("laptop", __name__)

    @laptop_blueprint.get("/laptops")
    def get_laptops():
        session = session_factory()
        page = request.args.get("page", 1, type=int)

        filters = {
            "max_price": request.args.get("max_price", type=int),
            "brand_id": request.args.get("brand_id", type=int),
            "os_id": request.args.get("os_id", type=int),
            "type_id": request.args.get("type_id", type=int),
            "display_size": request.args.get("display_size", type=int),
            "min_ram": request.args.get("min_ram", type=int),
            "min_storage": request.args.get("min_storage", type=int),
        }

        try:
            laptop_repository = SqlAlchemyLaptopRepository(session)
            get_laptops_use_case = GetLaptopsUseCase(laptop_repository)

            data = get_laptops_use_case.execute(page=page, filters=filters)

            return http_response(
                code=200,
                is_success=True,
                message="success to get laptops",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get laptops",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return laptop_blueprint
