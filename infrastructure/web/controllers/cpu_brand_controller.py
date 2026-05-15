# pyrefly: ignore [missing-import]
from flask import Blueprint
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_cpu_brands import GetCpuBrandsUseCase
from helpers.response import http_response
from infrastructure.database.repositories.cpu_brand_repository_impl import (
    SqlAlchemyCpuBrandRepository,
)


def create_cpu_brand_blueprint(session_factory):
    cpu_brand_blueprint = Blueprint("cpu_brand", __name__)

    @cpu_brand_blueprint.get("/cpu-brands")
    def get_cpu_brands():
        session = session_factory()
        try:
            cpu_brand_repository = SqlAlchemyCpuBrandRepository(session)
            get_cpu_brands_use_case = GetCpuBrandsUseCase(cpu_brand_repository)

            data = get_cpu_brands_use_case.execute()

            return http_response(
                code=200,
                is_success=True,
                message="success to get cpu brands",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get cpu brands",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return cpu_brand_blueprint
