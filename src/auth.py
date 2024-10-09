"""Authentication module."""

from __future__ import annotations

import bcrypt

import src.exceptions as custom_exceptions
from src.database.database import DataBaseManager


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
        if not password:
            raise custom_exceptions.PasswordDoesNotPresentError
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
        if not password:
            raise custom_exceptions.PasswordDoesNotPresentError
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password)


class Authenticator:
    """Class for authenticating users.

    Methods:
        authenticate(username: str, password: str)
    """

    def __init__(self) -> None:
        """Initialize authenticator."""
        self.encryptor = Encryptor()
        self.db_manager = DataBaseManager()

    async def authenticate(self, username: str, password: str) -> bool:
        """Check if user exists and password is correct.

        Args:
            username (str): name of user
            password (str): password given by user

        Returns:
            bool: True if user exists and password is correct, else False
        """
        user = await self._get_user_by_username(username)
        if user:
            return self.encryptor.check_password(password, user["password"])
        return False

    async def _get_user_by_username(self, username: str) -> dict[str, str] | None:
        user = await self.db_manager.get_user_by_username(username)
        if user:
            return dict(user)
        raise custom_exceptions.UserNotFoundError(username)
