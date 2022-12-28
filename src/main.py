from pathlib import Path
from sys import path

from fastapi import FastAPI
from mangum import Mangum


# fix the import path when the script is being called from pytest.
rootDir = Path(__file__).resolve().parent
path.append(str(rootDir))


app = FastAPI(docs_url=None)  # hide docs


@app.get("/")
async def root():
    """
    Get / endpoint
    """
    return {
        "message": "Hello from your backend service running on AWS Lambda!",
    }


# This is a wrapper for the FastAPI app that is used by AWS Lambda
handler = Mangum(app)
