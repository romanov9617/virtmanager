"""Module for singletone.

Singletone is a not realy good pattern,
and it most like a anti-pattern.
Nevertheless, I need to have only one
authorized user in every command handler.
"""

from typing import Self


class Singletone:
    """Singletone."""

    _instance = None

    def __new__(cls, *args, **kwargs) -> Self:  # noqa: ANN002, ANN003
        """Create new instance."""
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
