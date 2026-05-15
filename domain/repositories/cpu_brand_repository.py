from typing import Any, List, Protocol


class CpuBrandRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
