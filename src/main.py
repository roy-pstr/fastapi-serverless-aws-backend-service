import os
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
    running_on_aws_lambda = os.environ.get("AWS_EXECUTION_ENV") is not None
    message = "Hello from your backend service"
    if running_on_aws_lambda:
        message += " running on AWS Lambda!"
    else:
        message += " running on your local machine!"
    return {
        "message": message,
    }


# This is a wrapper for the FastAPI app that is used by AWS Lambda
handler = Mangum(app)
