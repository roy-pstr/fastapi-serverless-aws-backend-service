from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the FastAPI server.
    """
    LOGGER_LEVEL: str = "INFO"
    
    class Config:
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
