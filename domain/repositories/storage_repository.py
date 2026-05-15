from typing import Any, List, Protocol


class StorageRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
