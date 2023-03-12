from typing import Dict

from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def ping() -> Dict[str, str]:
    """
    Health Check.
    """
    return {"ping": "pong"}
