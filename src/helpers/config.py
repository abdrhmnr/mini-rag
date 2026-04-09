from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str
    FILE_ALLOWED_TYPES :list
    FILE_MAX_SIZE :int


    class Config:
        env_file = str(BASE_DIR / ".env")


def get_settings():
    return Settings()
