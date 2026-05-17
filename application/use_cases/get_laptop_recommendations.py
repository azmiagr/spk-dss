from typing import Dict, List, Optional

from domain.repositories.laptop_repository import LaptopRepository
from dss.engine import Criterion, SAWMethod

PER_PAGE = 10

PROFILES: Dict[str, Dict[str, float]] = {
    "gaming": {
        "C1": 0.20,
        "C2": 0.35,
        "C3": 0.05,
        "C4": 0.05,
        "C5": 0.05,
        "C6": 0.30,
    },
    "konten_kreator": {
        "C1": 0.25,
        "C2": 0.30,
        "C3": 0.05,
        "C4": 0.10,
        "C5": 0.05,
        "C6": 0.25,
    },
    "produktivitas": {
        "C1": 0.20,
        "C2": 0.10,
        "C3": 0.25,
        "C4": 0.20,
        "C5": 0.15,
        "C6": 0.10,
    },
    "dana_pelajar": {
        "C1": 0.15,
        "C2": 0.10,
        "C3": 0.20,
        "C4": 0.35,
        "C5": 0.10,
        "C6": 0.10,
    },
}

CRITERIA = [
    Criterion("C1", "benefit", 1.0),
    Criterion("C2", "benefit", 1.0),
    Criterion("C3", "benefit", 1.0),
    Criterion("C4", "cost",    1.0),
    Criterion("C5", "cost",    1.0),
    Criterion("C6", "cost",    1.0),
]


class GetLaptopRecommendationsUseCase:
    def __init__(self, laptop_repository: LaptopRepository):
        self.laptop_repository = laptop_repository

    def execute(self, profile: str, page: int = 1, filters: Optional[Dict] = None) -> dict:
        weights = PROFILES.get(profile)
        if weights is None:
            raise ValueError(f"Unknown profile: {profile}")

        laptops = self.laptop_repository.get_all_for_dss(filters=filters)

        criteria = [
            Criterion(c.code, c.type, weights[c.code])
            for c in CRITERIA
        ]

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

        ranked = SAWMethod().calculate(criteria, alternatives)

        total = len(ranked)
        start = (page - 1) * PER_PAGE
        end = start + PER_PAGE
        page_items = ranked[start:end]

        laptop_map = {laptop.id: laptop for laptop in laptops}

        items = []
        for item in page_items:
            laptop = laptop_map[item["id"]]
            items.append({
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
                "score": round(item["score"], 6),
            })

        return {
            "items": items,
            "page": page,
            "per_page": PER_PAGE,
            "total": total,
            "total_pages": -(-total // PER_PAGE),
            "profile": profile,
        }
