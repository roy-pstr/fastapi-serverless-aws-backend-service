from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import get_settings
from src.core.exception_handlers import http_exception_handler
from src.core.exception_handlers import request_validation_exception_handler
from src.core.exception_handlers import unhandled_exception_handler
from src.core.middleware import log_request_middleware


settings = get_settings()


def create_application() -> FastAPI:
    """
    Create the FastAPI application
    """
    application = FastAPI()

    # CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_HOSTS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.middleware("http")(log_request_middleware)
    application.add_exception_handler(RequestValidationError, request_validation_exception_handler)
    application.add_exception_handler(HTTPException, http_exception_handler)
    application.add_exception_handler(Exception, unhandled_exception_handler)

    return application


app: FastAPI = create_application()


@app.get("/")
async def root():
    """
    Root path
    """
    return {
        "message": "Hello from api v1!",
    }
