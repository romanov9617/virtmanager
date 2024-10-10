"""Module for common user `show` CLI command."""

from src.abstract import chain


class ShowCommandHandler(chain.BaseHandler):
    """Handler for `show` CLI command."""


class ShowMachinesHandler(chain.BaseHandler):
    """Handler for `show machines` CLI command."""
