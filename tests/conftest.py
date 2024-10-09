import pytest


@pytest.fixture
def user_with_admin_privileges_from_db():
    [
        ("username", "admin"),
        ("password", "admin"),
        ("salt", "admin"),
        ("is_superuser", True),
    ]


@pytest.fixture
def usual_user_from_db():
    pass
