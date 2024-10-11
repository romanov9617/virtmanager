"""Script for preparing database."""

import asyncio

from src.auth import Encryptor
from src.database.manager import Manager


def seed_db() -> None:
    """Seed database."""
    manager = Manager()
    asyncio.run(manager.create_database())
    asyncio.run(manager.create_user("admin", *Encryptor.hash_password("admin"), True))  # noqa: FBT003
