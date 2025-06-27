import logging
from functools import lru_cache
from pydantic_settings import BaseSettings
# from pydantic import AnyUrl
import os

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: str = os.environ.get("DATABASE_URL")


@lru_cache()
def get_settings() -> Settings:
    log.info("Loading config settings from the environment...")
    return Settings()
