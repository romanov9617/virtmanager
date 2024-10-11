"""Module for `show` CLI command."""

from __future__ import annotations

from src.abstract import chain
from src.cli import base
from src.database import monitor
from src.utils import make_table


class RootShowHandler(base.BasePasserHandler):
    """Handler for CLI command `show`."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "machines": RootShowMachineHandler,
            "components": RootShowComponentsHandler,
        }


class RootShowMachineHandler(base.BasePasserHandler):
    """Handler for CLI command `show machine`."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "--full": RootShowFullMachineHandler,
            "--short": RootShowMachineCharacteristicsHandler,
        }


class RootShowFullMachineHandler(chain.BaseHandler):
    """Handler for CLI command `show full machine`."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}

    async def handle(self, request: str | None = None) -> str | None:  # noqa: ARG002
        """Handle `show machine --full` command.

        Args:
            request (str | None, optional): None.
            Needs to accord with base class.
            Defaults to None.

        Returns:
            str | None: _description_
        """
        db_monitor = monitor.Monitor()
        machines = await db_monitor.get_all_machines_with_components()
        print(make_table(machines))


class RootShowMachineCharacteristicsHandler(chain.BaseHandler):
    """Handler for CLI command `show machine characteristics`."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}

    async def handle(self, request: str | None = None) -> str | None:  # noqa: ARG002
        """Handle `show machine characteristics` command.

        Args:
            request (str | None, optional): None.
            Needs to accord with base class. Defaults to None.

        Returns:
            str | None: _description_
        """
        db_monitor = monitor.Monitor()
        machines = await db_monitor.get_all_machines_with_characteristics()
        print(make_table(machines))


class RootShowComponentsHandler(base.BasePasserHandler):
    """Handler for CLI command `show components`."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "processors": RootShowProcessorsHandler,
            "rams": RootShowMemoryHandler,
            "hard_drives": RootShowHardDriveHandler,
        }


class RootShowProcessorsHandler(chain.BaseHandler):
    """Handler for CLI command `show components processors`."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}

    async def handle(self, request: str | None = None) -> str | None:  # noqa: ARG002
        """Handle `show components processors` command.

        Args:
            request (str | None, optional): None.
            Needs to accord with base class. Defaults to None.

        Returns:
            str | None: None. Log while function is working
        """
        db_monitor = monitor.Monitor()
        processors = await db_monitor.get_all_processors()
        print(make_table(processors))


class RootShowMemoryHandler(chain.BaseHandler):
    """Handler for CLI command `show memory`."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}

    async def handle(self, request: str | None = None) -> str | None:  # noqa: ARG002
        """Handle `show components memory` command.

        Args:
            request (str | None, optional): None.
            Needs to accord with base class. Defaults to None.

        Returns:
            str | None: None. Log while function is working
        """
        db_monitor = monitor.Monitor()
        memory = await db_monitor.get_all_memories()
        print(make_table(memory))


class RootShowHardDriveHandler(chain.BaseHandler):
    """Handler for CLI command `show hard_drive`."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}

    async def handle(self, request: str | None = None) -> str | None:  # noqa: ARG002
        """Handle `show components hard_drive` command.

        Args:
            request (str | None, optional): None.
            Needs to accord with base class. Defaults to None.

        Returns:
            str | None: None. Log while function is working
        """
        db_monitor = monitor.Monitor()
        hard_drives = await db_monitor.get_all_hard_drives()
        print(make_table(hard_drives))
