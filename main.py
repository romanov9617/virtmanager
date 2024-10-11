"""Entry point."""

import asyncio

from src.auth import Encryptor
from src.cli.cli import CLI
from src.database.manager import Manager

if __name__ == "__main__":
    cli = CLI()
    asyncio.run(cli())


def seed_db() -> None:
    """Seed database."""
    manager = Manager()
    asyncio.run(manager.create_database())
    asyncio.run(manager.create_user("admin", *Encryptor.hash_password("admin"), True))  # noqa: FBT003
