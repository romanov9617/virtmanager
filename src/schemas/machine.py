"""Define machine schemas.

Machine
Processor
Memory
HardDrive.
"""

from __future__ import annotations

from datetime import datetime  # noqa: TCH003
from uuid import UUID  # noqa: TCH003

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
    is_enabled: bool = True
    ip: str
    port: int
    os: str


class MachineCreateSchema(MachineSchemaBase):
    """Pydantic Machine schema to create."""

    processors: list[UUID] = []
    processors_usages: list[int] = []
    memories: list[UUID] = []
    memories_usages: list[int] = []
    hard_drives: list[UUID] = []
    hard_drives_usages: list[int] = []


class MachineReadSchema(MachineSchemaBase):
    """Pydantic Machine schema to read."""

    processors: list[ProcessorSchemaBase] = []
    memories: list[MemorySchemaBase] = []
    hard_drives: list[HardDriveSchemaBase] = []
    created_at: datetime
    updated_at: datetime | None = None
