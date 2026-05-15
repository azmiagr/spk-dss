from typing import Any, List, Protocol


class LaptopTypeRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
