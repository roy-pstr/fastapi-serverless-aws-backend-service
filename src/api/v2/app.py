from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

def create_application() -> FastAPI:

    app = FastAPI()

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    return app

app: FastAPI = create_application()


@app.get("/")
async def root():
    """
    Root path
    """
    return {
        "message": "Hello from api v2!",
    }
