"""Module for `create` CLI command."""

from __future__ import annotations

from typing import Callable, Self

from src.abstract import chain
from src.auth import Encryptor
from src.cli import base
from src.database import manager, monitor
from src.machine import creator
from src.schemas import machine, user
from src.utils import make_table


class RootCreateHandler(base.BasePasserHandler):
    """Handler for CLI command `create`."""

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {
            "machine": RootCreateMachineHandler,
            "user": RootCreateUserHandler,
        }


class RootCreateMachineHandler(chain.BaseHandler):
    """Handler for CLI command `create machine`."""

    async def handle(self, request: str | None = None) -> str | None:  # noqa: ARG002
        """Handle request with machine parameter.

        Args:
            request (str | None): None. Need to accord with base class

        Returns:
            str | None: None. Log while function is working
        """
        machine_data = await self.collect_data()
        concrete_creator = self._OS_MAPPER_CREATOR[machine_data.os.lower()](
            machine_data
        )
        await concrete_creator.create_machine()

    @property
    def _OS_MAPPER_CREATOR(self) -> dict[str, type[creator.Creator]]:  # noqa: N802
        return {
            "mac": creator.MacOSCreator,
            "windows": creator.WindowsCreator,
            "ubuntu": creator.UbuntuCreator,
        }

    async def collect_data(self) -> machine.MachineCreateSchema:
        """Collect data from user."""
        db_monitor = monitor.Monitor()
        name = input("Enter machine name: ")
        ip_address = input("Enter machine IP address: ")
        port = int(input("Enter machine port: "))
        os = input("Enter machine OS: ")
        hard_drives, hard_drives_usages = await self._choose_hard_drives(db_monitor)
        processors, processors_usages = await self._choose_processors(db_monitor)
        memories, memories_usages = await self._choose_memories(db_monitor)

        return machine.MachineCreateSchema(
            allias=name,
            ip=ip_address,
            port=port,
            hard_drives=hard_drives,
            hard_drives_usages=hard_drives_usages,
            processors=processors,
            processors_usages=processors_usages,
            memories=memories,
            memories_usages=memories_usages,
            os=os,
        )

    @staticmethod
    async def _choose_processors(
        db_monitor: monitor.Monitor,
    ) -> tuple[list[str], list[int]]:
        """Choose processors."""
        allowed_processors = await db_monitor.get_all_processors()
        print(make_table(allowed_processors))
        msg = """Choose processors UUID from table above and usage percent you want
separated by colon, UUID:usage.
Processors should be separated by space, for example uuid1:10 uuid2:20: """
        chosen_processors = [item.split(":") for item in input(msg).split()]
        processors = [processor[0] for processor in chosen_processors]
        processors_usages = [int(processor[1]) for processor in chosen_processors]
        return processors, processors_usages

    @staticmethod
    async def _choose_memories(
        db_monitor: monitor.Monitor,
    ) -> tuple[list[str], list[int]]:
        """Choose memories."""
        allowed_rams = await db_monitor.get_all_memories()
        print(make_table(allowed_rams))
        msg = """Choose RAM UUID from table above and usage percent you want
separated by colon, UUID:usage.
RAMs should be separated by space, for example uuid1:10 uuid2:20: """
        chosen_rams = [item.split(":") for item in input(msg).split()]
        rams = [ram[0] for ram in chosen_rams]
        rams_usages = [int(ram[1]) for ram in chosen_rams]
        return rams, rams_usages

    @staticmethod
    async def _choose_hard_drives(
        db_monitor: monitor.Monitor,
    ) -> tuple[list[str], list[int]]:
        """Choose hard drives."""
        allowed_hard_drives = await db_monitor.get_all_hard_drives()
        print(make_table(allowed_hard_drives))
        msg = """Choose HardDrive UUID from table above and usage percent you want
separated by colon, UUID:usage.
HardDrives should be separated by space, for example uuid1:10 uuid2:20: """
        chosen_hard_drives = [item.split(":") for item in input(msg).split()]
        hard_drives = [ram[0] for ram in chosen_hard_drives]
        hard_drives_usages = [int(ram[1]) for ram in chosen_hard_drives]
        return hard_drives, hard_drives_usages

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}


class RootCreateUserHandler(chain.BaseHandler):
    """Handler for CLI command `create user`."""

    @property
    def command_should_pass(self) -> dict[str | None, Callable | Self]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}

    async def handle(self, request: str | None = None) -> str | None:  # noqa: ARG002
        """Handle request with user parameter.

        Args:
            request (str | None): None. Need to accord with base class

        Returns:
            str | None: None. Log while function is working
        """
        db_manager = manager.Manager()
        user_data = await self.collect_data()
        data = self._prepare_data(user_data)
        await db_manager.create_user(*data)
        print("User successfully created")

    async def collect_data(self) -> user.UserCreateSchema:
        """Collect data from user."""
        username = input("Enter username: ")
        password = input("Enter password: ")
        return user.UserCreateSchema(username=username, password=password)

    def _prepare_data(self, user_data: user.UserCreateSchema) -> list[str]:
        hashed_password, salt = Encryptor.hash_password(password=user_data.password)
        return [user_data.username, hashed_password, salt, False]
