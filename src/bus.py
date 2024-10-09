"""Module describes bus."""

import abc
import socket

from logger import logger

from src.machine import Machine


class BusInterface(abc.ABC):
    """Abstract class for bus.

    Bus is responsible for communication with virtual machine.

    Methods:
        send_command(self, command: str) - send command to virtual machine
    """

    @staticmethod
    @abc.abstractmethod
    async def send_command(command: str, machine: Machine) -> None:
        """Abstract method for send command to virtual machine."""


class Bus(BusInterface):
    """Class for bus.

    Methods:
        send_command(command: str, machine: Machine) - send command to virtual machine
    """

    @staticmethod
    async def send_command(command: str, machine: Machine) -> None:
        """Send command to virtual machine."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((machine.ip, machine.port))
            s.sendall(command.encode())
            data = s.recv(1024)
            logger.info(f"{machine} responce: {data.decode()!r}")
