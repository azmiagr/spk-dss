from typing import Any, List, Protocol


class VgaBrandRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
