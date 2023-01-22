import os

from pathlib import Path
from sys import path

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
from src.core.middleware import log_request_middleware


settings = get_settings()

# fix the import path when the script is being called from pytest.
rootDir = Path(__file__).resolve().parent
path.append(str(rootDir))


def create_application() -> FastAPI:
    """
    Create the FastAPI application
    """
    application = FastAPI(docs_url=None)  # hide docs

    # add routers
    application.include_router(health_router, prefix="/ping", tags=["ping"])
    application.include_router(exceptions_router, prefix="/exceptions", tags=["exceptions"])

    application.middleware("http")(log_request_middleware)
    application.add_exception_handler(RequestValidationError, request_validation_exception_handler)
    application.add_exception_handler(HTTPException, http_exception_handler)
    application.add_exception_handler(Exception, unhandled_exception_handler)
    # mount sub-apps
    application.mount("/v1", app_v1)
    application.mount("/v2", app_v2)

    return application


app: FastAPI = create_application()


@app.get("/")
async def root():
    """
    Get / endpoint
    """
    running_on_aws_lambda = os.environ.get("AWS_EXECUTION_ENV") is not None
    return {
        "message": "Hello from your backend service",
        "stage": settings.STAGE,
        "machine": "AWS Lambda" if running_on_aws_lambda else "local machine",
    }


# This is a wrapper for the FastAPI app that is used by AWS Lambda
handler = Mangum(app)
