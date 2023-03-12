import logging

from src.core.config import get_settings


settings = get_settings()

logger = logging.getLogger("uvicorn")


def configure_logging(disable_uvicorn_access_logger: bool = True):
    # Disable uvicorn access logger
    if disable_uvicorn_access_logger:
        uvicorn_access = logging.getLogger("uvicorn.access")
        uvicorn_access.disabled = True

    # Set uvicorn logging level
    logger = logging.getLogger("uvicorn")
    logger.setLevel(logging.getLevelName(settings.LOGGER_LEVEL))
