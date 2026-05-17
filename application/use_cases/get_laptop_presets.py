from domain.repositories.laptop_repository import LaptopRepository
from dss.engine import Criterion, SAWMethod

from application.use_cases.get_laptop_recommendations import CRITERIA, PROFILES


class GetLaptopPresetsUseCase:
    def __init__(self, laptop_repository: LaptopRepository):
        self.laptop_repository = laptop_repository

    def execute(self, top: int = 3) -> dict:
        laptops = self.laptop_repository.get_all_for_dss()

        alternatives = [
            {
                "id": laptop.id,
                "name": laptop.name,
                "C1": laptop.ram_capacity,
                "C2": laptop.vga.gpu_benchmark_score,
                "C3": laptop.battery_backup,
                "C4": float(laptop.price),
                "C5": laptop.weight,
                "C6": laptop.processor.cpu_ranking_score,
            }
            for laptop in laptops
        ]

        laptop_map = {laptop.id: laptop for laptop in laptops}
        saw = SAWMethod()
        result = {}

        for profile_name, weights in PROFILES.items():
            criteria = [
                Criterion(c.code, c.type, weights[c.code])
                for c in CRITERIA
            ]
            ranked = saw.calculate(criteria, alternatives)

            result[profile_name] = [
                {
                    "rank": i + 1,
                    "laptop_id": item["id"],
                    "name": item["name"],
                    "score": round(item["score"], 6),
                    "price": str(laptop_map[item["id"]].price),
                    "brand_name": laptop_map[item["id"]].brand.name,
                    "processor": laptop_map[item["id"]].processor.name,
                    "vga": laptop_map[item["id"]].vga.name,
                    "ram_capacity": laptop_map[item["id"]].ram_capacity,
                    "display_size": laptop_map[item["id"]].display.size,
                }
                for i, item in enumerate(ranked[:top])
            ]

        return result
