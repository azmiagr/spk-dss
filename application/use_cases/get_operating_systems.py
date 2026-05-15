from typing import Union

from domain.repositories.operating_system_repository import OperatingSystemRepository


class GetOperatingSystemsUseCase:
    def __init__(self, operating_system_repository: OperatingSystemRepository):
        self.operating_system_repository = operating_system_repository

    def execute(self) -> list[dict[str, Union[int, str]]]:
        operating_systems = self.operating_system_repository.get_all()

        return [
            {
                "operating_system_id": operating_system.id,
                "name": operating_system.name,
            }
            for operating_system in operating_systems
        ]
