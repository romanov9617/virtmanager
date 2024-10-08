"""Enums module."""

from enum import Enum


class EnableStatus(Enum):
    """Enable status enum."""

    ENABLED = True
    DISABLED = False


class SuperUserEnum(Enum):
    """Superuser enum."""

    SUPERUSER = True
    USER = False
