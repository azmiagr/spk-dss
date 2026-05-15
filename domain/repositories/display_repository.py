from typing import Any, List, Protocol


class DisplayRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
