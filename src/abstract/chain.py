"""Chain of responsibility pattern.

I suppose we should use this pattern because it helps us
to build dynamic command handler.
You can add some new logic with time, for example,
    caching,
    check on new types of user and so on.
This pattern is rarely uses, but I think
it will be able to replace FastAPI dependency mechanism.
"""

from __future__ import annotations

import abc
from typing import Any, Callable, Self, Sequence

from src.auth import user


class Handler(abc.ABC):
    """Abstract class for handlers.

    Methods:
        set_next(self, handler: Self) - update next handler
        handle(self, request) - handle request
    """

    @abc.abstractmethod
    async def set_next(self, handler: Self) -> None:
        """Abstract method for update next handler.

        Args:
            handler (Self): next handler
        """

    @abc.abstractmethod
    async def handle(self, request: Any) -> Any | None:  # noqa: ANN401
        """Abstract method for handle request.

        Args:
            request (Any): requst we get from user

        Returns:
            Any | None: request for next handler
            if handle correctly, else - None
        """

    @property
    @abc.abstractmethod
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Abstract method for command should pass."""


class BaseHandler(Handler):
    """Base handler class.

    Define base behavior for all handlers.

    Methods:
        set_next(self, handler: Self) - update next handler
        handle(self, request) - handle request
    """

    USER = user

    def __init__(self) -> None:
        """Initialize handler."""
        self._next_handler: Self | None = None

    async def set_next(self, handler: Self | None) -> None:
        """Update next handler.

        Args:
            handler (Self | None): next handler
        """
        self._next_handler = handler

    @abc.abstractmethod
    async def handle(self, request: str | None = None) -> str | None:
        """Basic handle method.

        If there is next Handler - pass it to him,
        else - return None

        Args:
            request (Any): request we get from user

        Returns:
            Any | None: request for next handler
        """
        if self._next_handler:
            return await self._next_handler.handle(request)
        return None

    @property
    @abc.abstractmethod
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Get command should pass."""
        return {}

    def _pre_process_request(self, request: str) -> str | Sequence[str | bool]:
        """Pre process request."""
        return request
