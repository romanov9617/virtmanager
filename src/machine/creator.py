"""Module describes creator - Machine creating class.

Realized Factory pattern.
"""

import abc

from pydantic import BaseModel

from src.machine import product
from src.schemas import machine


class Creator(abc.ABC):
    """Abstract class for machine creator.

    Methods:
        factory_method(self) - abstract method for creating machine
        create_machine(self) - base logic for creating machine
    """

    def __init__(self, data: machine.MachineCreateSchema) -> None:
        """Initialize creator."""
        self.allias = data.allias
        self.ip = data.ip
        self.port = data.port

    @abc.abstractmethod
    def factory_method(self, data: BaseModel) -> product.Machine:
        """Abstract method for creating machine."""

    def create_machine(self, data: BaseModel) -> product.Machine:
        """Base logic for creating machine."""
        print("Creating machine...")
        return self.factory_method(data)


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
