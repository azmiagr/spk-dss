from typing import Any, List, Protocol


class VgaRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
