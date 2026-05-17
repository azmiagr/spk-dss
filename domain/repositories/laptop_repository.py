from typing import Any, List, Protocol


class LaptopRepository(Protocol):
    def get_all(self, page: int, per_page: int) -> List[Any]:
        ...

    def count(self) -> int:
        ...
