from typing import Union

from domain.repositories.storage_repository import StorageRepository


class GetStoragesUseCase:
    def __init__(self, storage_repository: StorageRepository):
        self.storage_repository = storage_repository

    def execute(self) -> list[dict[str, Union[int, str]]]:
        storages = self.storage_repository.get_all()

        return [
            {
                "storage_id": storage.id,
                "storage_type": storage.storage_type,
                "capacity": storage.capacity,
            }
            for storage in storages
        ]
