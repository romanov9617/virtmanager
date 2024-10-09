"""Database module."""

from __future__ import annotations

import aiofiles
import asyncpg

from src import enums
from src.config import Settings, settings


class DataBaseManager:
    """Database manager class.

    This class helps us to incapsulate all database logic.
    Also it unite all queries from `queries` folder.

    Methods:
        create_database(self) - run create_db.sql.
            This SQL code create all tables we need in database,
            and also seed all handbooks.
    """

    def __init__(self, config: Settings | None = None) -> None:
        """Initialize database manager.

        Args:
            config (Settings | None, optional): Settings object
            or another object we can get by dot notation. Defaults to None.
        """
        self._config = config or settings
        if not self._config:
            msg = "No config provided"
            raise ValueError(msg)

    async def _read_file(self, path: str) -> str:
        """Read file with non-blocking way.

        Args:
            path (str): file to path

        Returns:
            str: file content
        """
        async with aiofiles.open(path) as f:
            return await f.read()

    async def create_database(self) -> None:
        """Create all tables we need to correct work with database.

        It also seed

        Create tables:
            - machine
            - user
            - processor
            - hard_drive

        Create relations:
            - user_machine
            - processor_machine
            - hard_drive_machine
            - memory_machine
            - user_machine_access
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        create_db_query = await self._read_file("src/database/queries/create_db.sql")
        seed_handbooks_query = await self._read_file("src/database/queries/seed.sql")
        await conn.execute(create_db_query)
        await conn.execute(seed_handbooks_query)
        await conn.close()

    async def create_user(
        self,
        username: str,
        password: str,
        salt: str,
        is_superuser: enums.SuperUserEnum = enums.SuperUserEnum.USER,
    ) -> None:
        """Create new user in database.

        Args:
            username (str): user name
            password (str): user password
            salt (str): user salt
            is_superuser (bool): is superuser
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        create_user_query = await self._read_file("src/database/queries/add_user.sql")
        await conn.execute(
            create_user_query, username, password, salt, is_superuser.value
        )
        await conn.close()

    async def get_user_by_username(self, username: str) -> dict[str, str] | None:
        """Get user from database.

        Args:
            username (str): user name

        Returns:
            dict[str, str] | None: user data
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        get_user_query = await self._read_file(
            "src/database/queries/get_user_by_username.sql"
        )
        user = await conn.fetchrow(get_user_query, username)
        await conn.close()
        return user

    async def create_machine(
        self,
        name: str,
        ip: str,
        is_enabled: enums.EnableStatus = enums.EnableStatus.ENABLED,
    ) -> None:
        """Create new machine in database.

        Args:
            name (str): machine name
            ip (str): machine IP
            is_enabled (EnableStatus, optional): machine enable status.
            Defaults to EnableStatus.ENABLED.
        """
        conn = await asyncpg.connect(self._config.DB_URL)
        create_machine_query = await self._read_file(
            "src/database/queries/create_machine.sql"
        )
        await conn.execute(create_machine_query, name, is_enabled.value, ip)
