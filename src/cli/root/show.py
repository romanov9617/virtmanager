"""Module for `show` CLI command."""

from src.abstract import chain
from src.cli import base


class RootShowHandler(base.BasePasserHandler):
    """Handler for CLI command `show`."""


class RootShowMachineHandler(chain.BaseHandler):
    """Handler for CLI command `show machine`."""


class RootShowMachineComponentsHandler(chain.BaseHandler):
    """Handler for CLI command `show machine components`."""


class RootShowComponentsHandler(chain.BaseHandler):
    """Handler for CLI command `show components`."""
