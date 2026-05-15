from typing import Union

from domain.repositories.display_repository import DisplayRepository


class GetDisplaysUseCase:
    def __init__(self, display_repository: DisplayRepository):
        self.display_repository = display_repository

    def execute(self) -> list[dict[str, Union[int, str]]]:
        displays = self.display_repository.get_all()

        return [
            {
                "display_id": display.id,
                "size": display.size,
                "resolution": display.resolution,
                "refresh_rate": display.refresh_rate,
            }
            for display in displays
        ]
