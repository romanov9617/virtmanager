"""Module describes monitor.

Monitor is an object
that monitors every machine characteristics.

Monitor is responsible for making select queries in database
which can be used for machine efficiency, condition of machine and etc.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import asyncpg

from src.database.base import DatabaseBase
from src.exceptions import database as custom_exceptions

if TYPE_CHECKING:
    from src.config import Settings


class Monitor(DatabaseBase):
    """Monitor class.

    It is needed for monitoring database.

    Methods:
        get_all_machine_by_enable_status(self) - get all machines
        that are enabled at the moment.
    """

    def __init__(self, config: Settings | None = None) -> None:
        """Initialize monitor.

        Monitor is responsible for making select queries in database
        which can be used for machine efficiency, condition of machine and etc.

        Args:
            config (Settings | None, optional): Settings object. Defaults to None.

        Raises:
            custom_exceptions.QueryPathDoesNotProvidedError: Exception raised when
            path to folder with queries is not provided.
        """
        super().__init__(config)
        self.base_path_to_query = "src/database/analysis_queries/"
        if not self.base_path_to_query:
            raise custom_exceptions.QueryPathDoesNotProvidedError

    async def get_all_processors(self) -> list[asyncpg.Record]:
        """Get all processors from database.

        Returns:
            list[asyncpg.Record]: list of processors
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_all_processors_query = await self._read_file("get_all_processors.sql")
        processors = await conn.fetch(get_all_processors_query)
        await conn.close()
        return processors

    async def get_all_hard_drives(self) -> list[asyncpg.Record]:
        """Get all hard drives from database.

        Returns:
            list[asyncpg.Record]: List of hard drives
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_all_processors_query = await self._read_file("get_all_hard_drives.sql")
        processors = await conn.fetch(get_all_processors_query)
        await conn.close()
        return processors

    async def get_all_memories(self) -> list[asyncpg.Record]:
        """Get all RAMs from database.

        Returns:
            list[asyncpg.Record]: List of RAMs
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_all_processors_query = await self._read_file("get_all_memories.sql")
        processors = await conn.fetch(get_all_processors_query)
        await conn.close()
        return processors
