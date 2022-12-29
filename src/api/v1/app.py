from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.config import get_settings


settings = get_settings()

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Root path
    """
    return {
        "message": "Hello from api v1!",
    }