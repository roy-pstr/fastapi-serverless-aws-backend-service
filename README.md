# FastAPI Serverless AWS Backend Server
Welcome to the FastAPI Serverless AWS Backend Server project! This project is designed to provide a quick and easy way to get started with building a production ready backend server using the FastAPI web framework deployed on AWS lambda.

## Features
- Built with FastAPI, a modern, fast, and easy-to-use web framework for building APIs with Python
- Highly scalable and cost-effective hosting on AWS Lambda ([defualt limit](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html) is a total 1,000 concurrency across all functions in a region per account)
- Easy to deploy with the serverless framework
- Code quality ensured with static analysis tools Black, Mypy, iSort, Autoflake and Pylint
- Domain management per deployment stage - just provide a AWS Certificate ARN for your base domain
- Built-in monitoring with AWS CloudWatch for logs aggregation and AWS XRay for tracing

## Future Features
- Support in caching using FastAPI_Cache
- Basic authentication and authorization with Auth0
- Multi-stage CI/CD deployment with GitHub Actions
- Database migration support using Alembic
- Handling exceptions and logging

## Prerequisites
- An AWS account
- The [AWS CLI](https://aws.amazon.com/cli/) installed and configured
- [Python 3.7.2 or later](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/) for managing dependencies and packaging the app
- [npm](https://www.npmjs.com/) for installing the serverless framework and plugings
- [serverless](https://www.serverless.com/) framework for deploying the backend (just run `npm install -g serverless`)
- [Docker](https://www.docker.com/) for building and testing the app locally
- (Optional) An AWS Certificate of SSL/TLS certificate for a domain name in the AWS Certificate Manager ([this guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains-prerequisites.html) can help)

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
- Create the file: `touch .env`
- Set the following values inside:
```
TBA
```

4. Set access permissions to scripts directory
```bash
chmod 777 ./scripts/*
```

5. Run local code analysis
```
./scripts/check
```

6. Run local tests
```
./scripts/test
```

7. Run local server
```
./scripts/start
```

8. (Optional) If you want to use a custom domain for the backend, follow these steps:
- Obtain an ARN of AWS Certificate for your domain in the AWS Certificate Manager
- Set it on the `.env` file in `ACM_ARN`
- In `serverless.yml` -> set `customDomain.enabled: true`
- Update the value of `baseDomain` with your base domain
- Create the domain (this link a Route53 rule to the Certificate)
```
./scripts/create-domain
```
- Next time you will deploy the server will be exposed under your domain.

9. Deploy to AWS
```
./scripts/deploy
```

10. Remove deployment from AWS
```
./scripts/remove
```

11. (Optional) Remove the domain from Route53 (it will not remove the certificate!)
```
./scripts/delete-domain
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
