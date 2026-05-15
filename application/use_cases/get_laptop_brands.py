from typing import Union

from domain.repositories.laptop_brand_repository import LaptopBrandRepository


class GetLaptopBrandsUseCase:
    def __init__(self, laptop_brand_repository: LaptopBrandRepository):
        self.laptop_brand_repository = laptop_brand_repository

    def execute(self) -> list[dict[str, Union[int, str]]]:
        laptop_brands = self.laptop_brand_repository.get_all()

        return [
            {
                "laptop_brand_id": laptop_brand.id,
                "name": laptop_brand.name,
            }
            for laptop_brand in laptop_brands
        ]
