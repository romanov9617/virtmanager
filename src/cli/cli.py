"""Module for entry point of CLI."""

from __future__ import annotations

from typing import Callable, Self

from src.cli import auth, base, connection, show
from src.cli.root import root


class CLI(base.BasePasserHandler):
    """CLI is a handler for CLI command.

    At the moment, it does not handle any command, but pass it.
    But nevertheless, it can be extended to handle any command.

    Methods:
        __call__(self, *args: Any, **kwds: Any) -> str | None:  # noqa: ANN401, ARG002
            Run CLI and chain of handlers.

        handle(self, request: str) -> str | None:
            Handle reuquest coming to CLI.

        command_should_pass(self):
            property - dict with command should pass and corresponding handler
    """

    async def __call__(self) -> None:
        """Run CLI and chain of handlers.

        Returns:
            Any: result of command or None
        """
        while (request := input(">>> ")) != "exit":
            if request.strip() and request.split()[0] in self.command_should_pass:
                await self.handle(request)
            else:
                print("Unknown command")

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "auth": auth.AuthCommandHandler,
            "connect": connection.ConnectCommandHandler,
            "disconnect": connection.DisconnectCommandHandler,
            "show": show.ShowCommandHandler,
            "root": root.RootCommandHandler,
        }
