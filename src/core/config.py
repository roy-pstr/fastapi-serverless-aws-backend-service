import os

from functools import lru_cache
from typing import List
from typing import Literal

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the FastAPI server.
    """

    RUNNING_ON_AWS_LAMBDA: bool = os.environ.get("AWS_EXECUTION_ENV") is not None

    STAGE: Literal["dev", "staging", "prod"] = "dev"

    LOGGER_LEVEL: str = "INFO"

    ALLOWED_HOSTS: List[str] = ["*"]

    class Config:  # pylint: disable=too-few-public-methods
        """
        Tell BaseSettings the env file path
        """

        env_file = ".env"


@lru_cache()
def get_settings(**kwargs):
    """
    Get settings. ready for FastAPI's Depends.
    lru_cache - cache the Settings object per arguments given.
    """
    settings = Settings(**kwargs)
    return settings
