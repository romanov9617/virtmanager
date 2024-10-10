"""Module describes machines.

It contains classes for different types of machines.
Realized Factory pattern.
"""

from __future__ import annotations

import abc
import socket


class MachineInterface(abc.ABC):
    """Abstract class for machine."""

    @abc.abstractmethod
    async def listen(self) -> None:
        """Abstract method for listening from server."""

    @abc.abstractmethod
    def process_data(self, data: bytes, conn: socket.socket) -> None:
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

    async def listen(self) -> None:
        """Base method for listning from server."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.ip, self.port))
            while True:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    data = conn.recv(1024)
                    if data:
                        print(f"Received {data!r}")
                        self.process_data(data, conn)

    def process_data(self, data: bytes, conn: socket.socket) -> None:
        """Basic method for processing data from server.

        At default, it returns received data back again (echo)

        Args:
            data (bytes): some data from server
            conn (socket.socket): network connection
        """
        conn.sendall(data)


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

    def process_data(self, data: bytes, conn: socket.socket) -> None:
        """Process data from server.

        Ubuntu machine returns uppercase data back again

        Args:
            data (bytes): some data from server
            conn (socket.socket): network connection
        """
        conn.sendall(data.upper())


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

    def process_data(self, data: bytes, conn: socket.socket) -> None:
        """Process data from server.

        Windows machine returns titled case data back again

        Args:
            data (bytes): some data from server
            conn (socket.socket): network connection
        """
        conn.sendall(data.title())


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

    def process_data(self, data: bytes, conn: socket.socket) -> None:
        """Process data from server.

        Mac machine returns reversed data back again

        Args:
            data (bytes): some data from server
            conn (socket.socket): network connection
        """
        conn.sendall(data[::-1])
