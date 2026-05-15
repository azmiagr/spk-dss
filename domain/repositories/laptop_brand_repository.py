from typing import Any, List, Protocol


class LaptopBrandRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
