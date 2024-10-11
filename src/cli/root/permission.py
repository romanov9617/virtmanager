"""Module for `grant` and `revoke` CLI command."""

from __future__ import annotations

from typing import Sequence

from src.abstract import chain
from src.database import manager, monitor


class GrantCommnandHandler(chain.BaseHandler):
    """Handler for `grant` CLI command."""

    async def handle(self, request: str | None = None) -> str | None:
        """Handle request with user parameter."""
        db_manager = manager.Manager()
        if not request:
            return None
        params = self._pre_process_request(request)
        params = await self.prepare_data(params)
        await db_manager.grant_access(*params)
        return None

    def _pre_process_request(self, request: str) -> str | Sequence[str | bool]:
        machine_allias, username, admin = request.split(
            ":", maxsplit=2
        )  # machine_allias:username:{admin}
        is_admin = admin == "admin"
        return machine_allias, username, True, is_admin

    async def prepare_data(self, *args: Sequence[str | bool]) -> list[str]:
        """Prepare data for database query.

        Returns:
            list[str]: prepared data
        """
        db_manager = manager.Manager()
        db_monitor = monitor.Monitor()

        machine_allias: str
        username: str
        machine_allias, username, is_enabled, admin = args
        user = await db_manager.get_user_by_username(username)
        machine = await db_monitor.get_machine_by_allias(machine_allias)
        return [user["id"], machine["id"], is_enabled, admin]

    @property
    def command_should_pass(self) -> dict[str, type[chain.BaseHandler]]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}


class RevokeCommandHandler(chain.BaseHandler):
    """Handler for `revoke` CLI command."""

    async def handle(self, request: str | None = None) -> str | None:
        """Handle request with user parameter."""
        db_manager = manager.Manager()
        params = self._pre_process_request(request)
        params = await self.prepare_data(*params)
        await db_manager.revoke_user_access(*params)

    def _pre_process_request(self, request: str) -> str | list[str]:
        machine_allias, username = request.split(":", maxsplit=1)
        return [username, machine_allias]

    async def prepare_data(self, *args: list[str]) -> list[str]:
        """Prepare data for database query.

        Returns:
            list[str]: prepared data
        """
        db_manager = manager.Manager()
        db_monitor = monitor.Monitor()
        username, machine_allias = args
        user = await db_manager.get_user_by_username(username)
        machine = await db_monitor.get_machine_by_allias(machine_allias)
        return [user["id"], machine["id"]]

    @property
    def command_should_pass(self) -> dict[str, type[chain.BaseHandler]]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}
