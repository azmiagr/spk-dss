# pyrefly: ignore [missing-import]
from flask import Blueprint, request
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_laptop_presets import GetLaptopPresetsUseCase
from application.use_cases.get_laptop_recommendations import GetLaptopRecommendationsUseCase
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

    @laptop_blueprint.get("/laptops/recommend")
    def get_laptop_recommendations():
        session = session_factory()
        page = request.args.get("page", 1, type=int)
        profile = request.args.get("profile", type=str)
        order = request.args.get("order", "desc", type=str)

        if not profile:
            return http_response(
                code=400,
                is_success=False,
                message="query param 'profile' is required",
                data={},
            )

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
            use_case = GetLaptopRecommendationsUseCase(laptop_repository)

            data = use_case.execute(profile=profile, page=page, filters=filters, order=order)

            return http_response(
                code=200,
                is_success=True,
                message="success to get laptop recommendations",
                data=data,
            )
        except ValueError as exc:
            return http_response(
                code=400,
                is_success=False,
                message=str(exc),
                data={},
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get laptop recommendations",
                data={"detail": str(exc)},
            )
        finally:
            session.close()

    @laptop_blueprint.get("/laptops/presets")
    def get_laptop_presets():
        session = session_factory()
        top = request.args.get("top", 3, type=int)

        try:
            laptop_repository = SqlAlchemyLaptopRepository(session)
            use_case = GetLaptopPresetsUseCase(laptop_repository)

            data = use_case.execute(top=top)

            return http_response(
                code=200,
                is_success=True,
                message="success to get laptop presets",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get laptop presets",
                data={"detail": str(exc)},
            )
        finally:
            session.close()

    return laptop_blueprint
