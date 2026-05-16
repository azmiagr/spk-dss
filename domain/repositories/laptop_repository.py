from typing import Any, List, Protocol


class LaptopRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
