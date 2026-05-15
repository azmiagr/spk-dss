from typing import Union

from domain.repositories.cpu_brand_repository import CpuBrandRepository


class GetCpuBrandsUseCase:
    def __init__(self, cpu_brand_repository: CpuBrandRepository):
        self.cpu_brand_repository = cpu_brand_repository

    def execute(self) -> list[dict[str, Union[int, str]]]:
        cpu_brands = self.cpu_brand_repository.get_all()

        return [
            {
                "cpu_brand_id": cpu_brand.id,
                "name": cpu_brand.name,
            }
            for cpu_brand in cpu_brands
        ]
