# {{cookiecutter.project_name}}

{{cookiecutter.project_description}}

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
1. Install the dependencies
```
make install
```

2. Set up local environment in `.env` file
- Create the file: `touch .env`
- Set the following values inside:
```
TBA
```

3. Set access permissions to scripts directory
```bash
chmod 777 ./scripts/*
```

4. Run local code analysis
```
make check
```

5. Run local tests
```
make test
```

6. Run local server
```
make start
```
Test it </br>
`curl --request GET "https://localhost:8000"`

7. (Optional) If you want to use a custom domain for the backend, follow these steps:
- Obtain an ARN of AWS Certificate for your domain in the AWS Certificate Manager
- Set it on the `.env` file in `ACM_ARN`
- In `serverless.yml` -> set `customDomain.enabled: true`
- Update the value of `baseDomain` with your base domain
- Create the domain (this link a Route53 rule to the Certificate)
```
./scripts/create-domain
```
- Next time you will deploy the server will be exposed under your domain.

8. Deploy to AWS
```
make deploy
```
Test it </br>
`curl --request GET "https://<UNIQUE_ID>.execute-api.<AWS_REGION>.amazonaws.com/dev/"`

9. Remove deployment from AWS
```
make remove
```

10. (Optional) Remove the domain from Route53 (it will not remove the certificate!)
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

