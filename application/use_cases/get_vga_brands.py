from typing import Union

from domain.repositories.vga_brand_repository import VgaBrandRepository


class GetVgaBrandsUseCase:
    def __init__(self, vga_brand_repository: VgaBrandRepository):
        self.vga_brand_repository = vga_brand_repository

    def execute(self) -> list[dict[str, Union[int, str]]]:
        vga_brands = self.vga_brand_repository.get_all()

        return [
            {
                "vga_brand_id": vga_brand.id,
                "name": vga_brand.name,
            }
            for vga_brand in vga_brands
        ]
