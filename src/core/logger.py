import logging

from src.core.config import get_settings


settings = get_settings()

# Disable uvicorn access logger
uvicorn_access = logging.getLogger("uvicorn.access")
uvicorn_access.disabled = True

# Set uvicorn logging level
logger = logging.getLogger("uvicorn")
logger.setLevel(logging.getLevelName(settings.LOGGER_LEVEL))
