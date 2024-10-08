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
from typing import Any, Self


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


class BaseHandler(Handler):
    """Base handler class.

    Define base behavior for all handlers.

    Methods:
        set_next(self, handler: Self) - update next handler
        handle(self, request) - handle request
    """

    def __init__(self) -> None:
        """Initialize handler."""
        self._next_handler: Self | None = None

    async def set_next(self, handler: Self | None) -> None:
        """Update next handler.

        Args:
            handler (Self | None): next handler
        """
        self._next_handler = handler

    async def handle(self, request: Any) -> Any | None:  # noqa: ANN401
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
