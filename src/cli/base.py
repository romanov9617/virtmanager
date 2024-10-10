"""Module for base Handler with only pass destination to next handler."""

from __future__ import annotations

import abc
from typing import Callable, Self

from src.abstract import chain


class BasePasserHandler(chain.BaseHandler):
    """Handler just passing request to next handler."""

    async def __call__(self) -> Self | None:
        """Empty call method.

        Need to accord with base class
        """
        return self

    @property
    @abc.abstractmethod
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str | None, Callable | Self]: command should pass
                and corresponding handler
        """
        return {}

    async def handle(self, request: str | None = None) -> str | None:
        """Handle reuquest coming to CLI.

        Args:
            request (str): command from terminal

        Returns:
            str | None: result of command or None
        """
        if request:
            command, *args = self._pre_process_request(request)
        if command not in self.command_should_pass:
            return None

        handler = await self.command_should_pass[command]()
        await self.set_next(handler)
        print(f"Command: {command}")
        return await super().handle(*args)

    def _pre_process_request(self, request: str) -> list[str]:
        return request.split(maxsplit=1)
