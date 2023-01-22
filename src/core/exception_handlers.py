import sys, traceback

from typing import Union

from fastapi.exception_handlers import http_exception_handler as _http_exception_handler
from fastapi.exception_handlers import (
    request_validation_exception_handler as _request_validation_exception_handler,
)
from fastapi.responses import JSONResponse
from fastapi.responses import PlainTextResponse
from fastapi.responses import Response

from src.core.logger import logger


async def request_validation_exception_handler(request, exc) -> JSONResponse:
    """
    This is a wrapper to the default RequestValidationException handler of FastAPI.
    This function will be called when client input is not valid.
    """
    logger.debug("Our custom request_validation_exception_handler was called")
    body = await request.body()
    query_params = request.query_params._dict  # pylint: disable=protected-access
    detail = {"errors": exc.errors(), "body": body.decode(), "query_params": query_params}
    logger.info(detail)
    return await _request_validation_exception_handler(request, exc)


async def http_exception_handler(request, exc) -> Union[JSONResponse, Response]:
    """
    This is a wrapper to the default HTTPException handler of FastAPI.
    This function will be called when a HTTPException is explicitly raised.
    """
    logger.debug("Our custom http_exception_handler was called")
    return await _http_exception_handler(request, exc)


async def unhandled_exception_handler(request, exc) -> PlainTextResponse:
    """
    This middleware will log all unhandled exceptions.
    Unhandled exceptions are all exceptions that are not HTTPExceptions or RequestValidationErrors.
    """
    logger.debug("Our custom unhandled_exception_handler was called")
    exc_info = exception_and_traceback_info()
    host = getattr(getattr(request, "client", None), "host", None)
    port = getattr(getattr(request, "client", None), "port", None)
    url = f"{request.url.path}?{request.query_params}" if request.query_params else request.url.path
    logger.error(
        f'{host}:{port} - "{request.method} {url}" 500 Internal Server Error [{exc_info.get("errorType")}: {exc_info.get("errorMessage")}]'
    )
    logger.error("Exception in ASGI application\n" + exc_info.get("stackTrace", ""))
    return PlainTextResponse(str(exc), status_code=500)


def exception_and_traceback_info() -> dict:
    """
    This function returns a dictionary with the exception type, message and traceback.
    """
    exception_type, exception_value, exception_traceback = sys.exc_info()
    traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
    return {
        "errorType": getattr(exception_type, "__name__", None),
        "errorMessage": str(exception_value),
        "stackTrace": "".join(traceback_string),
    }
