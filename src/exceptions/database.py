"""Exceptions that can be raised in `database` package."""


class ConfigDoesNotProvidedError(Exception):
    """Config does not provided exception."""

    def __init__(self) -> None:
        """Initialize exception."""
        super().__init__("Config does not provided")


class DBUrlDoesNotProvidedError(Exception):
    """DB url does not provided exception."""

    def __init__(self) -> None:
        """Initialize exception."""
        super().__init__("DB url does not provided")


class QueryPathDoesNotProvidedError(Exception):
    """Base path does not provided exception."""

    def __init__(self) -> None:
        """Initialize exception."""
        super().__init__("Base path does not provided")
