# FastAPI Serverless AWS Backend Server
<p align="center">
<img src="assets/sls_lambda_fastapi.png" data-canonical-src="assets/sls_lambda_fastapi.png" width=400/>
</p>

This project act as a template for a FastAPI server deployed on AWS Lambda for production use.


## Features
- Project structure template
- FastAPI boiler plate code:
  - Root application with versioning API (currently V1 and V2 are defined)
  - Middleware for CORS, exceptions and logging
  - Config module with settings loaded from your `.env` file
  - Logs are working also in production environment (AWS Lambda)
  - Test suite setup with TestClient
  - Health check route and exceptions routes
 - Python code quality tools already setup both locally and as part of the CI (Pylint, Black, Isort, MyPy)
 - Dockerfile with AWS lambda base image for the FastAPI service container
 - Poetry for python environment management
 - Serverless.yml boiler plate:
   - Lambda function for the FastAPI backend service
   - Lambda is container-based and images are deployed to AWS ECR
   - Defined cloud watch IAM roles and retention policy (30 days)
   - Defined XRay IAM roles
   - Custom domain management support in three sub-domains, one per stage.
  - Scripts folder so you can easily run it all
   
## Future Features
- Boiler plate code for caching using FastAPI_Cache
- Basic authentication and authorization with Auth0
- Database migration support using Alembic

## Prerequisites
- An AWS account
- The [AWS CLI](https://aws.amazon.com/cli/) installed and configured
- [Python 3.7.2 or later](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/) for managing dependencies and packaging the app
- [npm](https://www.npmjs.com/) for installing the serverless framework and plugins
- [serverless](https://www.serverless.com/) framework for deploying the backend (just run `npm install -g serverless`)
- [Docker](https://www.docker.com/) for building and testing the app locally
- (Optional) An AWS Certificate of SSL/TLS certificate for a domain name in the AWS Certificate Manager ([this guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains-prerequisites.html) can help)

## Getting Started
1. First, install cookiecutter if you don't already have it:
```
python3 -m pip install cookiecutter
```
Then, in the directory you want your project to be:
```
cookiecutter gh:roy-pstr/fastapi-serverless-aws-backend-service
```
You will be asked to put a few variables:
<details><summary>Input Variables</summary>

- project_name [default FastAPI Serverless AWS Backend Service]
- directory_name [default fastapi-serverless-aws-backend-service] - this is your project directory
- project_description
- service_name [default FastAPIServerlessAWSBackendService] - this is your service name in AWS (see serverless.yml)
- base_domain [default your.domain] - this is the base domain for any api url that will be deployed (only in case you will enable the domain deployment) (https://api.base_domain, https://api-dev.base_domain ... )
- ecr_repository_base_name [default fastapi-serverless-aws-backend-service]
- lambda_docker_image_tag [default fastapi-serverless-aws-backend-service]
- log_retention_in_days [default 30] - This is the retention for the cloud watch logs in AWS

</details>

2. Install the dependencies
```
cd {{directory_name}}
make install
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
make check
```

6. Run local tests
```
make test
```

7. Run local server
```
make start
```
Test it </br>
`curl --request GET "https://localhost:8000"`

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
make deploy
```
Test it </br>
`curl --request GET "https://<UNIQUE_ID>.execute-api.<AWS_REGION>.amazonaws.com/dev/"`

10. Remove deployment from AWS
```
make remove
```

11. (Optional) Remove the domain from Route53 (it will not remove the certificate!)
```
./scripts/delete-domain
```

## Environments
What | How (script) | Where (endpoint)
--- | --- | --- 
**Local** | `./scripts/start` | `http://localhost:8000`
**Remote**|`./scripts/deploy`|`https://***.execute-api.<AWS_REGION>.amazonaws.com/dev/`
**Develop Domain**|`./scripts/create-domain`</br>`./scripts/deploy`|`https://api-develop.your.domain`
**Staging Domain**|`./scripts/create-domain staging`</br>`./scripts/deploy staging`|`https://api-staging.your.domain`
**Production Domain**|`./scripts/create-domain prod`</br>`./scripts/deploy prod`|`https://api.your.domain`

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
