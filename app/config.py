from pathlib import Path
from pydantic import BaseSettings, PostgresDsn, validator

PROJECT_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    # POSTGRESQL DATABASE CONFIG
    POSTGRES_HOSTNAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    POSTGRES_DATABASE_URI: str = ""

    @validator("POSTGRES_DATABASE_URI")
    def create_db_uri(cls, v, values):
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_HOSTNAME"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('POSTGRES_DB')}",
        )

    # FASTAPI CONFIG
    SERVER_HOST: str
    SERVER_PORT: int

    # BITRIX CONFIG
    BITRIX_WEBHOOK: str

    class Config:
        env_file = PROJECT_DIR / "config.env"
        case_sensitive = True
        env_file_encoding = "utf-8"


settings: Settings = Settings()
