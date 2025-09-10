from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = BASE_DIR / ".env"


class DatabaseSettings(BaseSettings):
    name: str
    user: str
    password: str
    host: str
    port: int

    model_config = SettingsConfigDict(env_file=ENV_FILE, env_prefix="DB_", extra="ignore")

    @property
    def url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.user}:{self.password}@"
            f"{self.host}:{self.port}/{self.name}"
        )


class Settings(BaseSettings):
    base_dir: Path = BASE_DIR

    db: DatabaseSettings = DatabaseSettings()  # noqa

    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")
