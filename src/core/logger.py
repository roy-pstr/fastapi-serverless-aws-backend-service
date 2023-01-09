import logging

from src.core.config import get_settings


settings = get_settings()

logger = logging.getLogger("uvicorn")
logger.setLevel(eval(f"logging.{settings.LOGGER_LEVEL}"))
