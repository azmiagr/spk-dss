# pyrefly: ignore [missing-import]
from flask import Blueprint
# pyrefly: ignore [missing-import]
from sqlalchemy.exc import SQLAlchemyError

from application.use_cases.get_storages import GetStoragesUseCase
from helpers.response import http_response
from infrastructure.database.repositories.storage_repository_impl import (
    SqlAlchemyStorageRepository,
)


def create_storage_blueprint(session_factory):
    storage_blueprint = Blueprint("storage", __name__)

    @storage_blueprint.get("/storages")
    def get_storages():
        session = session_factory()

        try:
            storage_repository = SqlAlchemyStorageRepository(session)
            get_storages_use_case = GetStoragesUseCase(storage_repository)

            data = get_storages_use_case.execute()

            return http_response(
                code=200,
                is_success=True,
                message="success to get storages",
                data=data,
            )
        except SQLAlchemyError as exc:
            return http_response(
                code=500,
                is_success=False,
                message="failed to get storages",
                data={
                    "detail": str(exc),
                },
            )
        finally:
            session.close()

    return storage_blueprint
