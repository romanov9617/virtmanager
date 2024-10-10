"""Module for `auth` CLI command."""

from __future__ import annotations

from typing import Callable, Self

from src.abstract import chain
from src.auth import Authenticator
from src.cli import base
from src.schemas.user import UserCreateSchema


class AuthCommandHandler(base.BasePasserHandler):
    """Class for passing auth command."""

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Dict with command should pass and corresponding handler.

        Can handle only with flags --json, --password, --yaml
        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "--password": AuthPasswordHandler,
        }


class AuthPasswordHandler(chain.BaseHandler):
    """Handler for --password flag."""

    def __init__(self) -> None:
        """Initialize handler."""
        self.authenticator = Authenticator()

    async def handle(self, request: str | None = None) -> str | None:
        """Handle request with --password flag.

        Args:
            request (str): username:password string

        Returns:
            str | None: desicion if user is authorized or not
        """
        user = self._pre_process_request(request)
        if await self.authenticator.authenticate(user.username, user.password):
            print(f"User {user.username} authorized")
            return "Authorized"
        print("Wrong username or password")
        return "Wrong username or password"

    def _pre_process_request(self, request: str | None = None) -> UserCreateSchema:
        while not request:
            request = input("Enter username:password: ")
        username, password = request.split(":")
        return UserCreateSchema(username=username, password=password)

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {"--password": self}
