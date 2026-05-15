# pyrefly: ignore [missing-import]
from flask import Blueprint
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_vga_brands import GetVgaBrandsUseCase
from helpers.response import http_response
from infrastructure.database.repositories.vga_brand_repository_impl import (
    SqlAlchemyVgaBrandRepository,
)


def create_vga_brand_blueprint(session_factory):
    vga_brand_blueprint = Blueprint("vga_brand", __name__)

    @vga_brand_blueprint.get("/vga-brands")
    def get_vga_brands():
        session = session_factory()

        try:
            vga_brand_repository = SqlAlchemyVgaBrandRepository(session)
            get_vga_brands_use_case = GetVgaBrandsUseCase(vga_brand_repository)

            data = get_vga_brands_use_case.execute()

            return http_response(
                code=200,
                is_success=True,
                message="success to get vga brands",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get vga brands",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return vga_brand_blueprint
