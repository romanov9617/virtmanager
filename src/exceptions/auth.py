"""Exceptions that can be raised in `auth` module."""


class UserNotFoundError(Exception):
    """User not found exception."""

    def __init__(self, username: str) -> None:
        """Initialize exception."""
        super().__init__(f"User with username: {username} not found")


class PasswordDoesNotPresentError(Exception):
    """Password does not present exception."""

    def __init__(self) -> None:
        """Initialize exception."""
        super().__init__("Password does not present")
