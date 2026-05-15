from typing import Union

from domain.repositories.processor_repository import ProcessorRepository


class GetProcessorsUseCase:
    def __init__(self, processor_repository: ProcessorRepository):
        self.processor_repository = processor_repository

    def execute(self) -> list[dict[str, Union[int, str]]]:
        processors = self.processor_repository.get_all()

        return [
            {
                "processor_id": processor.id,
                "name": processor.name,
                "cpu_ranking_score": processor.cpu_ranking_score,
                "brand_name": processor.brand.name,
            }
            for processor in processors
        ]
