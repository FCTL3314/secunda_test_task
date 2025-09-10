from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent
ENV_FILE: Path = BASE_DIR / ".env"


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


class ApiSettings(BaseSettings):
    static_api_key: str

    model_config = SettingsConfigDict(env_file=ENV_FILE, env_prefix="API_", extra="ignore")


class Settings(BaseSettings):
    base_dir: Path = BASE_DIR

    db: DatabaseSettings = DatabaseSettings()
    api: ApiSettings = ApiSettings()

    model_config = SettingsConfigDict(env_file=ENV_FILE, extra="ignore")


settings: Settings = Settings()
