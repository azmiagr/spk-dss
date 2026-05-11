from os import name
from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Optional

@dataclass
class LaptopCatalog:
    id: Optional[int]
    name: str

@dataclass
class LaptopType:
    id: Optional[int]
    name: str

@dataclass
class OperatingSystem:
    id: Optional[int]
    name: str

@dataclass
class CpuBrand:
    id: Optional[int]
    name: str

@dataclass
class Processor:
    id: Optional[int]
    brand_id: int
    name: str
    cpu_ranking_score: int

@dataclass
class VgaBrand:
    id: Optional[int]
    name: str

@dataclass
class Vga:
    id: Optional[int]
    name: str
    brand_id: int
    gpu_benchmark_score: int
    memory_capacity: int

@dataclass
class Display:
    id: Optional[int]
    size: int
    resolution: str
    refresh_rate: int

@dataclass
class Storage:
    id: Optional[int]
    storage_type: str
    capacity: int

@dataclass
class LaptopStorage:
    laptop_id: int
    storage_id: int

@dataclass
class Criterion:
    id: Optional[int]
    criteria_code: str
    name: str
    attribute_type: str
    default_weight: int

@dataclass
class Laptop:
    id: Optional[int]
    name: str
    brand_id: int
    type_id: int
    os_id: int
    processor_id: int
    vga_id: int
    display_id: int
    ram_capacity: int
    ram_type: str
    price: Decimal
    weight: int
    battery_backup: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


    