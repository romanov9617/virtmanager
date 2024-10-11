"""Define user schemas."""

from __future__ import annotations

from datetime import datetime  # noqa: TCH003

import pydantic

from src.schemas.machine import MachineSchemaBase  # noqa: TCH001


class UserSchemaBase(pydantic.BaseModel):
    """Pydantic User base schema."""

    username: str


class UserCreateSchema(UserSchemaBase):
    """Pydantic User create schema.

    Only username and password.
    Can be used for registration and login.
    """

    password: str


class UserReadSchema(UserSchemaBase):
    """Pydantic User read schema.

    Full information about user.
    """

    is_superuser: bool = False
    created_at: datetime
    updated_at: datetime | None = None
    machines_authorized: list[MachineSchemaBase] = []
    machines_denied: list[MachineSchemaBase] = []
    machines_allowed: list[MachineSchemaBase] = []
    machines_admin: list[MachineSchemaBase] = []
