from typing import Union

from domain.repositories.vga_repository import VgaRepository


class GetVgasUseCase:
    def __init__(self, vga_repository: VgaRepository):
        self.vga_repository = vga_repository

    def execute(self) -> list[dict[str, Union[int, str]]]:
        vgas = self.vga_repository.get_all()

        return [
            {
                "vga_id": vga.id,
                "name": vga.name,
                "brand_name": vga.brand.name,
                "gpu_benchmark_score": vga.gpu_benchmark_score,
                "memory_capacity": vga.memory_capacity,
            }
            for vga in vgas
        ]
