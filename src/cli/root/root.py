"""Module for `root` CLI command."""

from __future__ import annotations

from typing import Callable, Self

from src.cli import base
from src.cli.root import create, permission, show


class RootCommandHandler(base.BasePasserHandler):
    """Handler for CLI command `root`."""

    async def __call__(self) -> Self | None:
        """Empty call method."""
        return await super().__call__()

    async def handle(self, request: str | None = None) -> str | None:
        """Handle reuquest coming to CLI.

        Args:
            request (str): command from terminal

        Returns:
            str | None: result of command or None
        """
        if self.USER.is_superuser:
            return await super().handle(request)
        print("Only superuser can use this command")
        return None

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "create": create.RootCreateHandler,
            "show": show.RootShowHandler,
            "grant": permission.GrantCommnandHandler,
            "revoke": permission.RevokeCommandHandler,
        }
