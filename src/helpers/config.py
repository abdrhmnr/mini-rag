from __future__ import annotations  # ← لازم أول سطر في الملف

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPEN_API_KEY: str
    FILE_ALLOWED_TYPES: List[str]
    FILE_MAX_SIZE: int

    class Config:
        env_file = ".env"        # ← بدون فاصلة!
        env_file_encoding = "utf-8"
        extra = "ignore"


def get_settings():
    return Settings()