"""Module for `connect` and `disconnect` CLI commands."""

from src.abstract import chain


class ConnectCommandHandler(chain.BaseHandler):
    """Handler for `connect` CLI command."""


class DisconnectCommandHandler(chain.BaseHandler):
    """Handler for `disconnect` CLI command."""
