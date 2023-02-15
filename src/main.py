from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.exceptions import RequestValidationError
from mangum import Mangum

from src.api.exceptions import router as exceptions_router
from src.api.health import router as health_router
from src.api.v1.app import app as app_v1
from src.api.v2.app import app as app_v2
from src.core.config import get_settings
from src.core.exception_handlers import http_exception_handler
from src.core.exception_handlers import request_validation_exception_handler
from src.core.exception_handlers import unhandled_exception_handler
from src.core.logger import configure_logging
from src.core.middleware import log_request_middleware


settings = get_settings()


def create_application() -> FastAPI:
    """
    Create the FastAPI application
    """
    # configure logging
    configure_logging(disable_uvicorn_access_logger=True)

    # create the FastAPI application
    application = FastAPI(docs_url=None)  # hide docs

    # add routers
    application.include_router(health_router, prefix="/ping", tags=["ping"])
    application.include_router(exceptions_router, prefix="/exceptions", tags=["exceptions"])

    # add exception handlers and middleware
    application.middleware("http")(log_request_middleware)
    application.add_exception_handler(RequestValidationError, request_validation_exception_handler)
    application.add_exception_handler(HTTPException, http_exception_handler)
    application.add_exception_handler(Exception, unhandled_exception_handler)

    # mount sub-apps (those used for versioning)
    application.mount("/v1", app_v1)
    application.mount("/v2", app_v2)

    return application


app: FastAPI = create_application()


@app.get("/")
async def root():
    """
    Get / endpoint
    """
    return {
        "message": "Hello from your backend service",
        "stage": settings.STAGE,
        "machine": "AWS Lambda" if settings.RUNNING_ON_AWS_LAMBDA else "local machine",
    }


# This is a wrapper for the FastAPI app that is used by AWS Lambda
handler = Mangum(app)
