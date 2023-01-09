import json, sys, time, traceback

from fastapi import Request
from fastapi.responses import PlainTextResponse

from src.core.logger import logger


async def measure_time(request: Request, call_next):
    """
    This middleware will log all requests and their processing time.
    E.g. log:
    0.0.0.0:1234 - GET /ping 200 1.00ms
    """
    logger.debug("middleware: measure_time")
    url = f"{request.url.path}?{request.query_params}" if request.query_params else request.url.path
    start_time = time.time()
    response = await call_next(request)
    process_time = (time.time() - start_time) * 1000
    formatted_process_time = "{0:.2f}".format(process_time)
    host = getattr(getattr(request, "client", None), "host", None)
    port = getattr(getattr(request, "client", None), "port", None)
    logger.info(f"{host}:{port} - {request.method} {url} {response.status_code} {formatted_process_time}ms")
    return response


async def handle_unhandled_exceptions(request: Request, call_next):
    """
    This middleware will log all unhandled exceptions.
    Prevents from teh server to crash - instead it will return a 500 status code response and log all error details.
    """
    # pylint: disable=broad-except
    logger.debug("middleware: handle_unhandled_exceptions")
    url = ""
    try:
        url = f"{request.url.path}?{request.query_params}" if request.query_params else request.url.path
        response = await call_next(request)
        return response
    except Exception as exc:
        exception_type, exception_value, exception_traceback = sys.exc_info()
        traceback_string = traceback.format_exception(exception_type, exception_value, exception_traceback)
        host = getattr(getattr(request, "client", None), "host", None)
        port = getattr(getattr(request, "client", None), "port", None)
        err_msg = json.dumps(
            {
                "request": f"{host}:{port} - {request.method} {url}",
                "errorType": getattr(exception_type, "__name__", None),
                "errorMessage": str(exception_value),
                "stackTrace": traceback_string,
            }
        )
        logger.error(err_msg)
        return PlainTextResponse(str(exc), status_code=500)
