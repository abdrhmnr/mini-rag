from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPEN_API_KEY: str

    class Config:
        env_file=".env",
        env_file_encoding="utf-8"
        extra="ignore"


def get_settings():
    return Settings()