"""Database base module."""

from __future__ import annotations

import aiofiles

from src.config import Settings, settings
from src.exceptions import database as custom_exceptions


class DatabaseBase:
    """Database base class.

    This class is base class needed for inheritence.
    It describe common logic for every classes
    which is used for working with database

    Methods:
        read_file(self, file_name: str) -> str - read file with non-blocking way
    """

    def __init__(self, config: Settings | None = None) -> None:
        """Initialize database manager.

        Args:
            config (Settings | None, optional): Settings object
            or another object we can get by dot notation. Defaults to None.
        """
        self._config = config or settings
        self.base_path_to_query: str | None = None
        if not self._config:
            raise custom_exceptions.ConfigDoesNotProvidedError
        if not self._config.DB_URL:
            raise custom_exceptions.DBUrlDoesNotProvidedError

    async def _read_file(self, file_name: str) -> str:
        """Read file with non-blocking way.

        Args:
            file_name (str): file to path

        Returns:
            str: file content
        """
        if not self.base_path_to_query:
            raise custom_exceptions.QueryPathDoesNotProvidedError
        path = self.base_path_to_query + file_name
        async with aiofiles.open(path) as f:
            return await f.read()
