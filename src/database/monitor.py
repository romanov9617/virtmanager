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

    async def get_all_machines(self) -> list[asyncpg.Record]:
        """Get all machines from database.

        Returns:
            list[asyncpg.Record]: List of machines
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_all_machines_query = await self._read_file("get_all_machines.sql")
        machines = await conn.fetch(get_all_machines_query)
        await conn.close()
        return machines

    async def get_machine_by_allias(self, allias: str) -> list[asyncpg.Record]:
        """Get machine by allias from database.

        Args:
            allias (str): Allias of machine

        Returns:
            list[asyncpg.Record]: List of machines
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_machine_by_allias_query = await self._read_file("get_machine_by_allias.sql")
        machines = await conn.fetchrow(get_machine_by_allias_query, allias)
        await conn.close()
        return machines

    async def get_machine_by_ip(self, ip: str) -> list[asyncpg.Record]:
        """Get machine by ip from database.

        Args:
            ip (str): IP of machine

        Returns:
            list[asyncpg.Record]: List of machines
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_machine_by_ip_query = await self._read_file("get_machine_by_ip.sql")
        machines = await conn.fetch(get_machine_by_ip_query, ip)
        await conn.close()
        return machines

    async def get_all_users(self) -> list[asyncpg.Record]:
        """Get all users from database.

        Returns:
            list[asyncpg.Record]: List of users
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_all_users_query = await self._read_file("get_all_users.sql")
        users = await conn.fetch(get_all_users_query)
        await conn.close()
        return users

    async def get_allowed_machines(self, *args: list[str]) -> list[asyncpg.Record]:
        """Get allowed machines from database.

        Args:
            *args (list[str]): username

        Returns:
            list[asyncpg.Record]: List of allowed machines
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_allowed_machines_query = await self._read_file("get_allowed_machines.sql")
        username = args[0]
        allowed_machines = await conn.fetch(get_allowed_machines_query, username)
        await conn.close()
        return allowed_machines

    async def get_all_machines_with_components(self) -> list[asyncpg.Record]:
        """Get all machines with components from database.

        Returns:
            list[asyncpg.Record]: List of machines
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_machines_with_components_query = await self._read_file(
            "get_all_machines_with_components.sql"
        )
        machines = await conn.fetch(get_machines_with_components_query)
        await conn.close()
        return machines

    async def get_all_machines_with_characteristics(self) -> list[asyncpg.Record]:
        """Get all machines with characteristics from database.

        Returns:
            list[asyncpg.Record]: List of machines
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_machines_with_characteristics_query = await self._read_file(
            "get_all_machines_with_characteristics.sql"
        )
        machines = await conn.fetch(get_machines_with_characteristics_query)
        await conn.close()
        return machines

    async def get_all_machines_user_admin(
        self, *args: list[str]
    ) -> list[asyncpg.Record]:
        """Get all machines from database.

        Args:
            *args (list[str]): username

        Returns:
            list[asyncpg.Record]: List of machines
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_all_machines_user_admin_query = await self._read_file(
            "get_all_machines_user_admin.sql"
        )
        username = args[0]
        machines = await conn.fetch(get_all_machines_user_admin_query, username)
        await conn.close()
        return machines

    async def get_all_machines_user_allowed(
        self, *args: list[str]
    ) -> list[asyncpg.Record]:
        """Get all machines from database.

        Args:
            *args (list[str]): username

        Returns:
            list[asyncpg.Record]: List of machines
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_all_machines_user_allowed_query = await self._read_file(
            "get_all_machines_user_allowed.sql"
        )
        username = args[0]
        machines = await conn.fetch(get_all_machines_user_allowed_query, username)
        await conn.close()
        return machines
