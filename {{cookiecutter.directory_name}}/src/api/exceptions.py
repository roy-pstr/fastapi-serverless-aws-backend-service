from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get("/http_exception")
async def httpexception():
    """
    Example for HTTPException raised from inside the endpoint.
    """
    raise HTTPException(
        status_code=500,
        detail="StarletteHTTPException raised from inside the endpoint.",
    )


@router.get("/type_validation_exception/{value}")
async def type_validation(value: int):
    """
    Example for ValidationError that will be triggered if value is not 'int'
    """
    return value


@router.get("/unhandled_exception")
async def unhandled():
    """
    Example for unhandled error raised from inside the endpoint.
    """
    raise ValueError("Value error raised from inside the endpoint.")


@router.get("/status_code/400")
async def status_code_400():
    """
    Example for returning status code 400 (without raising an exception)
    """
    return JSONResponse(status_code=400, content={"reason": "Status code 400"})


@router.get("/status_code/500")
async def status_code_500():
    """
    Example for returning status code 500 (without raising an exception)
    """
    return JSONResponse(status_code=500, content={"reason": "Status code 500"})
