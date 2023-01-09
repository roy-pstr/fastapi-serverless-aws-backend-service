from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def create_application() -> FastAPI:
    """
    Create the FastAPI application
    """
    application = FastAPI()

    # CORS
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return application


app: FastAPI = create_application()


@app.get("/")
async def root():
    """
    Root path
    """
    return {
        "message": "Hello from api v2!",
    }
