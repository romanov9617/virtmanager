from unittest.mock import MagicMock, patch, AsyncMock
from contextlib import nullcontext as does_not_raise

import pytest
import bcrypt

from src.auth import Authenticator, Encryptor
from src.exceptions import UserNotFoundError, PasswordDoesNotPresentError


class TestEncryptor:

    @pytest.mark.parametrize(
        ("password", "salt", "expected_result", "expected_exception"),
        [
            ("password", None, bytes, does_not_raise()),
            ("password", bcrypt.gensalt(), bytes, does_not_raise()),
            (None, None, None, pytest.raises(PasswordDoesNotPresentError)),
            (None, bcrypt.gensalt(), None, pytest.raises(PasswordDoesNotPresentError)),
        ],
    )
    def test_hash_password(self, password, salt, expected_result, expected_exception):
        with expected_exception:
            hashed_password = Encryptor.hash_password(password, salt)
            assert isinstance(hashed_password, expected_result)

    def test_check_password(self):
        password = "password"
        salt = None
        hashed_password = Encryptor.hash_password(password, salt)
        assert Encryptor.check_password(password, hashed_password)


class TestAuthenticator:


    async def test_get_user_by_username(self, user_with_admin_privileges_from_db):
        authenticator = Authenticator()
        authenticator.db_manager.get_user_by_username = AsyncMock(
            return_value=user_with_admin_privileges_from_db
        )
        user = await authenticator._get_user_by_username("admin")
        assert user == user_with_admin_privileges_from_db
