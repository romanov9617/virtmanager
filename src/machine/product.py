"""Module describes machines.

It contains classes for different types of machines.
Realized Factory pattern.
"""

from __future__ import annotations

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from asyncio import StreamReader, StreamWriter


class MachineInterface(abc.ABC):
    """Abstract class for machine."""

    @abc.abstractmethod
    async def listen(self, reader: StreamReader, writer: StreamWriter) -> None:
        """Abstract method for listening from server."""

    @abc.abstractmethod
    def process_data(self, data: bytes, writer: StreamWriter) -> None:
        """Process data from server."""


class Machine(MachineInterface):
    """Class for machine."""

    def __init__(self, allias: str, ip: str, port: int) -> None:
        """Initialize machine.

        Args:
            allias (str): machine name
            ip (str): machine IP address
            port (int): machine port
        """
        self.allias = allias
        self.ip = ip
        self.port = port
        self.os: str | None = None

    def __str__(self) -> str:
        """String representation of machine."""
        return f"{self.allias} {self.ip}:{self.port} {self.os}"

    async def listen(self, reader: StreamReader, writer: StreamWriter) -> None:
        """Base method for listning from server.

        Args:
            reader (asyncio.StreamReader): network connection
            writer (asyncio.StreamWriter): network connection
        """
        while True:
            data = await reader.read(1024)
            if not data:
                break
            self.process_data(data, writer)

    def process_data(self, data: bytes, writer: StreamWriter) -> None:
        """Basic method for processing data from server.

        At default, it returns received data back again (echo)

        Args:
            data (bytes): some data from server
            writer (asyncio.StreamWriter): network connection
        """
        writer.write(data)


class UbuntuMachine(Machine):
    """Class for Ubuntu machine."""

    def __init__(self, allias: str, ip: str, port: int) -> None:
        """Initialize Ubuntu machine.

        Args:
            allias (str): name of machine
            ip (str): machine IP address
            port (int): machine port
        """
        super().__init__(allias, ip, port)
        self.os = "Ubuntu"

    def process_data(self, data: bytes, writer: StreamWriter) -> None:
        """Process data from server.

        Ubuntu machine returns uppercase data back again

        Args:
            data (bytes): some data from server
            writer (asyncio.StreamWriter): network connection
        """
        writer.write(data.upper())


class WindowsMachine(Machine):
    """Class for Windows machine."""

    def __init__(self, allias: str, ip: str, port: int) -> None:
        """Initialize Windows machine.

        Args:
            allias (str): name of machine
            ip (str): machine IP address
            port (int): machine port
        """
        super().__init__(allias, ip, port)
        self.os = "Windows"

    def process_data(self, data: bytes, writer: StreamWriter) -> None:
        """Process data from server.

        Windows machine returns titled case data back again

        Args:
            data (bytes): some data from server
            writer (asyncio.StreamWriter): network connection
        """
        writer.write(data.title())


class MacMachine(Machine):
    """Class for Mac machine."""

    def __init__(self, allias: str, ip: str, port: int) -> None:
        """Initialize Mac machine.

        Args:
            allias (str): name of machine
            ip (str): machine IP address
            port (int): machine port
        """
        super().__init__(allias, ip, port)
        self.os = "MacOS"

    def process_data(self, data: bytes, writer: StreamWriter) -> None:
        """Process data from server.

        Mac machine returns reversed data back again

        Args:
            data (bytes): some data from server
            writer (asyncio.StreamWriter): network connection
        """
        writer.write(data[::-1])
