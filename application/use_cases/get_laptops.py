from domain.repositories.laptop_repository import LaptopRepository

PER_PAGE = 10


class GetLaptopsUseCase:
    def __init__(self, laptop_repository: LaptopRepository):
        self.laptop_repository = laptop_repository

    def execute(self, page: int = 1) -> dict:
        total = self.laptop_repository.count()
        laptops = self.laptop_repository.get_all(page=page, per_page=PER_PAGE)

        return {
            "items": [
                {
                    "laptop_id": laptop.id,
                    "name": laptop.name,
                    "brand_name": laptop.brand.name,
                    "type_name": laptop.type.name,
                    "operating_system": laptop.operating_system.name,
                    "processor": laptop.processor.name,
                    "vga": laptop.vga.name,
                    "display_size": laptop.display.size,
                    "display_resolution": laptop.display.resolution,
                    "display_refresh_rate": laptop.display.refresh_rate,
                    "storages": [
                        {
                            "storage_type": link.storage.storage_type,
                            "capacity": link.storage.capacity,
                        }
                        for link in laptop.storage_links
                    ],
                    "ram_capacity": laptop.ram_capacity,
                    "ram_type": laptop.ram_type,
                    "price": str(laptop.price),
                    "weight": laptop.weight,
                    "battery_backup": laptop.battery_backup,
                }
                for laptop in laptops
            ],
            "page": page,
            "per_page": PER_PAGE,
            "total": total,
            "total_pages": -(-total // PER_PAGE),
        }
