# FastAPI Serverless AWS Backend Server
Welcome to the FastAPI Serverless AWS Backend Server project! This project is designed to provide a quick and easy way to get started with building a production ready backend server using the FastAPI web framework and deploying it to AWS using serverless technology.

## Features
- Built with FastAPI, a modern, fast, and easy-to-use web framework for building APIs with Python
- Uses AWS Lambda, ECR and API Gateway to deploy the serverless backend
- Easy to deploy with the serverless framework

## Future Features
- Support in API versions
- Support in caching using FastAPI_Cache
- Automatic HTTPS with AWS Certificate Manager
- Basic authentication and authorization with Auth0
- Automated testing and deployment with GitHub Actions
- Code quality ensured with static analysis tools Black, Mypy, iSort, Autoflake and Pylint

## Prerequisites
- An AWS account
- The [AWS CLI](https://aws.amazon.com/cli/) installed and configured
- [Python 3.7 or later](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/) for managing dependencies and packaging the app
- [npm](https://www.npmjs.com/) for installing the serverless framework and plugings
- [serverless](https://www.serverless.com/) framework for deploying the backend (just run `npm install -g serverless`)
- [Docker](https://www.docker.com/) for building and testing the app locally

## Getting Started
1. Clone the repository
```
git clone https://github.com/larium/fastapi-serverless-aws-backend.git
```

2. Install the dependencies
```
cd fastapi-serverless-aws-backend
npm install
poetry install
```

3. Set up local environment in `.env` file
```

```
4. Run local code analysis
```
poetry run pytest
```

4. Run local tests
```
chmod 777 ./scripts/test # only once
./scripts/test
```

5. Run local server
```
poetry run uvicorn ...
```

6. Deploy to AWS
```
sls deploy
```

## Contributing
We welcome contributions to this project! If you have an idea for a new feature or improvement, please open an issue or pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Tips
### Set python interpreter in VScode
- Run `poetry run which python` and copy the python path
- `command+shift+p` to open the VScode command shortcuts and enter `Python: Select Interpreter`
- Select `+ Enter interpreter path...` and paste the python path
- That's it.
