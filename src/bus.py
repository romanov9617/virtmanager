"""Module describes bus."""

import abc
import asyncio

from logger import logger

from src.machine.product import Machine


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
    async def send_commands(machine_ip: str, machine_port: int) -> None:
        """Send commands to virtual machine.

        Args:
            machine_ip (str): machine IP address
            machine_port (int): machine port
        """
        reader, writer = await asyncio.open_connection(machine_ip, machine_port)

        while True:
            command = input()
            if command == "exit":
                break
            writer.write(command.encode())
            await writer.drain()
            response = await reader.read(1024)
            logger.info(f"Machine {machine_ip}:{machine_port} -> { response.decode() }")

        writer.close()
        await writer.wait_closed()
        print("Writer closed")
