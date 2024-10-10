"""Module for `create` CLI command."""

from __future__ import annotations

from typing import Callable, Self

from src.abstract import chain
from src.cli import base
from src.database import monitor
from src.utils import make_table


class RootCreateHandler(base.BasePasserHandler):
    """Handler for CLI command `create`."""

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "machine": RootCreateMachineHandler,
            "user": RootCreateUserHandler,
        }


class RootCreateMachineHandler(chain.BaseHandler):
    """Handler for CLI command `create machine`."""

    async def handle(self, request: str | None = None) -> str | None:  # noqa: ARG002
        """Handle request with machine parameter.

        Args:
            request (str): username:password string

        Returns:
            str | None: desicion if user is authorized or not
        """
        db_monitor = monitor.Monitor()

        allowed_processors = await db_monitor.get_all_processors()
        print(make_table(allowed_processors))
        msg = "Choose processors UUID separated by space from table above: "
        chosen_processors = input(msg).split()

        allowed_memories = await db_monitor.get_all_memories()
        print(make_table(allowed_memories))
        msg = "Choose RAMs UUID separated by space from table above: "
        chosen_memories = input(msg).split()

        allowed_hard_drives = await db_monitor.get_all_hard_drives()
        print(make_table(allowed_hard_drives))
        msg = "Choose HardDrives UUID separated by space from table above: "
        chosen_hard_drives = input(msg).split()
        return " ".join(chosen_processors + chosen_memories + chosen_hard_drives)

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}


class RootCreateUserHandler(chain.BaseHandler):
    """Handler for CLI command `create user`."""
