"""Module describes bus."""

import abc
import socket

from logger import logger


class BusInterface(abc.ABC):
    """Abstract class for bus.

    Bus is responsible for communication with virtual machine.

    Methods:
        send_command(self, command: str) - send command to virtual machine
    """

    @abc.abstractmethod
    async def send_command(self, command: str) -> None:
        """Abstract method for send command to virtual machine."""


class Bus(BusInterface):
    """Class for bus.

    Methods:
        send_command(self, command: str) - send command to virtual machine
    """

    async def send_command(self, command: str) -> None:
        """Send command to virtual machine."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(("127.0.0.1", 7100))
            s.sendall(command.encode())
            data = s.recv(1024)
            logger.info(f"Received: {data.decode()!r}")
