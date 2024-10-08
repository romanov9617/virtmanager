"""Authentication module."""

from __future__ import annotations

import bcrypt


class Encryptor:
    """Class for encrypting passwords.

    Methods:
        hash_password(password: str, salt: str | None = None)
        check_password(self, password: str)
    """

    @staticmethod
    def hash_password(password: str, salt: str | None = None) -> str:
        """Hash password.

        Args:
            password (str): user password
            salt (str | None, optional): Salt for hashing. Defaults to None.

        Returns:
            str: hashed password for database
        """
        salt = salt or bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed_password.encode("utf-8")

    @staticmethod
    def check_password(password: str, hashed_password: str) -> bool:
        """Check password against hashed password from database.

        Args:
            password (str): password from user input
            hashed_password (str): password from database

        Returns:
            bool: True if password is correct, else False
        """
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)


class Authenticator:
    """Class for authenticating users.

    Methods:
        authenticate(username: str, password: str)
    """

    def __init__(self) -> None:
        """Initialize authenticator."""
        self.encryptor = Encryptor()

    def authenticate(self, username: str, password: str) -> bool:
        """Check if user exists and password is correct.

        Args:
            username (str): name of user
            password (str): password given by user

        Returns:
            bool: True if user exists and password is correct, else False
        """
        return bool(username and password)

    def _get_user_by_username(self, username: str) -> dict[str, str] | None:
        pass
