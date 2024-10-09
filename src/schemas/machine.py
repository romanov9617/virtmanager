"""Define machine schemas.

Machine
Processor
Memory
HardDrive.
"""

from datetime import datetime

import pydantic


class ProcessorSchemaBase(pydantic.BaseModel):
    """Pydantic Processor base schema."""

    name: str
    num_nuclears: int
    frequency: int
    max_temperature: int


class MemorySchemaBase(pydantic.BaseModel):
    """Pydantic Memory base schema."""

    type: str
    capacity: int
    frequency: int
    service_life_end: str
    warantee_period_end: str


class HardDriveSchemaBase(pydantic.BaseModel):
    """Pydantic HardDrive base schema."""

    type: str
    capacity: int
    frequency: int
    service_life_end: str
    warantee_period_end: str


class MachineSchemaBase(pydantic.BaseModel):
    """Pydantic Machine base schema."""

    allias: str
    is_enabled: bool
    ip: str
    created_at: datetime
    updated_at: datetime
