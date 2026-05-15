from typing import Union

from domain.repositories.laptop_type_repository import LaptopTypeRepository


class GetLaptopTypesUseCase:
    def __init__(self, laptop_type_repository: LaptopTypeRepository):
        self.laptop_type_repository = laptop_type_repository

    def execute(self) -> list[dict[str, Union[int, str]]]:
        laptop_types = self.laptop_type_repository.get_all()

        return [
            {
                "laptop_type_id": laptop_type.id,
                "name": laptop_type.name,
            }
            for laptop_type in laptop_types
        ]
