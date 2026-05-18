from typing import Any, Dict, List, Optional, Protocol


class LaptopRepository(Protocol):
    def get_all(self, page: int, per_page: int, filters: Optional[Dict] = None) -> List[Any]:
        ...

    def count(self, filters: Optional[Dict] = None) -> int:
        ...

    def get_all_for_dss(self, filters: Optional[Dict] = None) -> List[Any]:
        ...
