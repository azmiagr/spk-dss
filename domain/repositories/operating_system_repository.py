from typing import Any, List, Protocol


class OperatingSystemRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
