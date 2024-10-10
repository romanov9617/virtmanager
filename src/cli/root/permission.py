"""Module for `grant` and `revoke` CLI command."""

from src.abstract import chain


class GrantCommnandHandler(chain.BaseHandler):
    """Handler for `grant` CLI command."""


class RevokeCommandHandler(chain.BaseHandler):
    """Handler for `revoke` CLI command."""
