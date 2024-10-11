"""Entry point."""

import asyncio

from src.cli.cli import CLI

if __name__ == "__main__":
    cli = CLI()
    asyncio.run(cli())
