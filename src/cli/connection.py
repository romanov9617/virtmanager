"""Module for `connect` and `disconnect` CLI commands."""

from __future__ import annotations

import asyncio

from src.abstract import chain
from src.bus import Bus
from src.cli import base
from src.database import monitor
from src.machine import creator
from src.schemas import machine as machine_schema


class ConnectCommandHandler(base.BasePasserHandler):
    """Handler for `connect` CLI command."""

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {"--allias": ConnectAlliasHandler}


class ConnectAlliasHandler(chain.BaseHandler):
    """Handler for `--allias` flag."""

    async def handle(self, request: str | None = None) -> str | None:
        """Handle reuquest coming to CLI."""
        db_monitor = monitor.Monitor()

        machine = await db_monitor.get_machine_by_allias(request)
        host = machine["ip"]
        port = machine["port"]
        os = machine["os"]
        machine_data = machine_schema.MachineCreateSchema(
            allias=request, ip=host, port=port, os=os
        )
        creator = self._OS_MAPPER_CREATOR[os](machine_data)
        machine = await creator.create_machine(only_object=True)
        print(machine)
        server = await asyncio.start_server(machine.listen, host, port)
        await Bus.send_commands(host, port)
        server.close()

    @property
    def command_should_pass(self) -> dict[str, chain.BaseHandler]:
        """Property - dict with command should pass and corresponding handler.

        Returns:
            dict[str, Callable]: command should pass and corresponding handler
        """
        return {None: self}

    @property
    def _OS_MAPPER_CREATOR(self) -> dict[str, type[creator.Creator]]:  # noqa: N802
        return {
            "mac": creator.MacOSCreator,
            "windows": creator.WindowsCreator,
            "ubuntu": creator.UbuntuCreator,
        }
