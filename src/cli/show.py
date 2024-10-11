"""Module for common user `show` CLI command."""

from __future__ import annotations

from src.abstract import chain
from src.cli import base
from src.database import monitor
from src.utils import make_table


class ShowCommandHandler(base.BasePasserHandler):
    """Handler for `show` CLI command."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "machines": ShowMachinesHandler,
        }


class ShowMachinesHandler(base.BasePasserHandler):
    """Handler for `show machines` CLI command."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "allowed": ShowAllowedMachinesHandler,
            "admin": ShowAdminMachinesHandler,
        }


class ShowAllowedMachinesHandler(chain.BaseHandler):
    """Handler for `show machines allowed` CLI command."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}

    async def handle(self, request: str | None = None) -> None:  # noqa: ARG002
        """Handle `show machines allowed` command.

        Args:
            request (str | None, optional): None.
            Needs to accord with base class. Defaults to None.
        """
        db_monitor = monitor.Monitor()
        if not self.USER.is_superuser:
            machines = await db_monitor.get_all_machines_user_allowed(self.USER.id)
        else:
            machines = await db_monitor.get_all_machines()
        print(make_table(machines))


class ShowAdminMachinesHandler(chain.BaseHandler):
    """Handler for `show machines admin` CLI command."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}

    async def handle(self, request: str | None = None) -> None:  # noqa: ARG002
        """Handle `show machines admin` command.

        Args:
            request (str | None, optional): None.
            Needs to accord with base class. Defaults to None.
        """
        db_monitor = monitor.Monitor()
        if not self.USER.is_superuser:
            machines = await db_monitor.get_all_machines_user_admin(self.USER.id)
        else:
            machines = await db_monitor.get_all_machines()
        print(make_table(machines))
