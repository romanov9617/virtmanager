"""Authentication module."""

from __future__ import annotations

from typing import TYPE_CHECKING

import bcrypt

from src.abstract import singletone
from src.database.manager import Manager
from src.exceptions import auth as custom_exceptions
from src.schemas import user as user_schema

if TYPE_CHECKING:
    from uuid import UUID


class Encryptor:
    """Class for encrypting passwords.

    Methods:
        hash_password(password: str, salt: str | None = None)
        check_password(self, password: str)
    """

    @staticmethod
    def hash_password(password: str, salt: str | None = None) -> tuple[str, str]:
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
        return hashed_password, salt

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
        self.db_manager = Manager()

    async def authenticate(self, username: str, password: str) -> User | None:
        """Check if user exists and password is correct.

        Args:
            username (str): name of user
            password (str): password given by user

        Returns:
            bool: True if user exists and password is correct, else False
        """
        user = await self._get_user_by_username(username)
        if user and self.encryptor.check_password(password, user["password"]):
            return user_schema.UserReadSchema(**user)
        return None

    async def _get_user_by_username(self, username: str) -> dict[str, str] | None:
        user = await self.db_manager.get_user_by_username(username)
        if user:
            return dict(user)
        return None


class User(singletone.Singletone):
    """User class."""

    def __init__(self) -> None:
        """Initialize user."""
        self.id: UUID | None = None
        self.username = ""
        self.is_superuser = False
        self.machines_admin: list[user_schema.MachineSchemaBase] = []
        self.machines_allowed: list[user_schema.MachineSchemaBase] = []
        self.machines_denied: list[user_schema.MachineSchemaBase] = []
        self.machines_authorized: list[user_schema.MachineSchemaBase] = []

    def update(self, data: user_schema.UserReadSchema) -> None:
        """Update user data.

        Args:
            data (user_schema.UserUpdateSchema): user data
        """
        if data.id:
            self.id = data.id
        if data.is_superuser:
            self.is_superuser = data.is_superuser
        if data.username:
            self.username = data.username
        if data.machines_admin:
            self.machines_admin = data.machines_admin
        if data.machines_allowed:
            self.machines_allowed = data.machines_allowed
        if data.machines_denied:
            self.machines_denied = data.machines_denied
        if data.machines_authorized:
            self.machines_authorized = data.machines_authorized

    def downgrade(self) -> None:
        """Downgrade user data."""
        self.id = None
        self.username = ""
        self.is_superuser = False
        self.machines_admin = []
        self.machines_allowed = []
        self.machines_denied = []
        self.machines_authorized = []

    def __str__(self) -> str:
        """String representation of user."""
        return f"{self.username}"


user = User()
