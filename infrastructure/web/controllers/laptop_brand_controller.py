# pyrefly: ignore [missing-import]
from flask import Blueprint
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_laptop_brands import GetLaptopBrandsUseCase
from helpers.response import http_response
from infrastructure.database.repositories.laptop_brand_repository_impl import (
    SqlAlchemyLaptopBrandRepository,
)


def create_laptop_brand_blueprint(session_factory):
    laptop_brand_blueprint = Blueprint("laptop_brand", __name__)

    @laptop_brand_blueprint.get("/laptop-brands")
    def get_laptop_brands():
        session = session_factory()

        try:
            laptop_brand_repository = SqlAlchemyLaptopBrandRepository(session)
            get_laptop_brands_use_case = GetLaptopBrandsUseCase(laptop_brand_repository)

            data = get_laptop_brands_use_case.execute()

            return http_response(
                code=200,
                is_success=True,
                message="success to get laptop brands",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get laptop brands",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return laptop_brand_blueprint
