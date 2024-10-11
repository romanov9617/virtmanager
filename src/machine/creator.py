"""Module describes creator - Machine creating class.

Realized Factory pattern.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

from src.database import monitor
from src.database.manager import Manager
from src.machine import product

if TYPE_CHECKING:
    from src.schemas import machine


class Creator(abc.ABC):
    """Abstract class for machine creator.

    Methods:
        factory_method(self) - abstract method for creating machine
        create_machine(self) - base logic for creating machine
    """

    def __init__(self, data: machine.MachineCreateSchema) -> None:
        """Initialize creator."""
        self.data = data
        self.manager = Manager()
        self.monitor = monitor.Monitor()

    @abc.abstractmethod
    def factory_method(self) -> product.Machine:
        """Abstract method for creating machine."""

    async def create_machine(self) -> product.Machine:
        """Base logic for creating machine."""
        print("Creating machine...")
        machine_data = self._prepare_machine_data(self.data)
        if not await self.monitor.get_machine_by_allias(self.data.allias):
            await self.manager.create_machine(*machine_data)
        print("Machine created")
        return self.factory_method(self.data)

    def _prepare_machine_data(
        self, data: machine.MachineCreateSchema
    ) -> list[str, list[str | int]]:
        return [
            data.allias,
            data.ip,
            data.port,
            data.hard_drives,
            data.hard_drives_usages,
            data.processors,
            data.processors_usages,
            data.memories,
            data.memories_usages,
            data.os,
        ]


class UbuntuCreator(Creator):
    """Concrete class for Ubuntu machine creation."""

    def factory_method(
        self, data: machine.MachineCreateSchema
    ) -> product.UbuntuMachine:
        """Create Ubuntu machine."""
        return product.UbuntuMachine(data.allias, data.ip, data.port)


class WindowsCreator(Creator):
    """Concrete class for Windows machine creation."""

    def factory_method(
        self, data: machine.MachineCreateSchema
    ) -> product.WindowsMachine:
        """Create Windows machine."""
        return product.WindowsMachine(data.allias, data.ip, data.port)


class MacOSCreator(Creator):
    """Concrete class for Mac machine creation."""

    def factory_method(self, data: machine.MachineCreateSchema) -> product.MacMachine:
        """Create Mac machine."""
        return product.MacMachine(data.allias, data.ip, data.port)
