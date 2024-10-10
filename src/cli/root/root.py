"""Module for `root` CLI command."""

from __future__ import annotations

from typing import Callable, Self

from src.cli import base
from src.cli.root import create, delete, permission, show


class RootCommandHandler(base.BasePasserHandler):
    """Handler for CLI command `root`."""

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "create": create.RootCreateHandler,
            "delete": delete.RootDeleteHandler,
            "list": show.RootShowHandler,
            "grant": permission.GrantCommnandHandler,
            "revoke": permission.RevokeCommandHandler,
        }
