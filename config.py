"""Configuration for the application."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration for the application.

    DB_HOST: str - postgres database host
    DB_PORT: int - postgres database port
    DB_USER: str - postgres database user
    DB_PASSWORD: str - postgres database password
    DB_NAME: str - postgres database name
    """

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )

    @property
    def DB_URL(self) -> str:  # noqa: N802
        """Property for PostgreSQL database URL.

        It used asyncpg driver for PostgreSQL database.

        Returns:
            str: PostgreSQL database URL.
        """
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
