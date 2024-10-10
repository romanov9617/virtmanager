"""Module for `delete` CLI command."""

from __future__ import annotations

from typing import Callable, Self

from src.abstract import chain
from src.cli import base


class RootDeleteHandler(base.BasePasserHandler):
    """Handler for CLI command `delete`."""

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "machine": RootDeleteMachineHandler,
            "user": RootDeleteUserHandler,
        }


class RootDeleteMachineHandler(chain.BaseHandler):
    """Handler for CLI command `delete machine`."""


class RootDeleteUserHandler(chain.BaseHandler):
    """Handler for CLI command `delete user`."""
