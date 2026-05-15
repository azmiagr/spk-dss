from typing import Any, List, Protocol


class ProcessorRepository(Protocol):
    def get_all(self) -> List[Any]:
        ...
