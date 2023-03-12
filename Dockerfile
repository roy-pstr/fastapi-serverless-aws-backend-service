FROM public.ecr.aws/lambda/python:3.9
ENV POETRY_VERSION=1.3.2
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# install poetry
RUN pip install -U pip \
    pip install poetry==$POETRY_VERSION
RUN poetry --version
RUN poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml ${LAMBDA_TASK_ROOT}/
RUN cd ${LAMBDA_TASK_ROOT} && poetry install --no-interaction --no-ansi --no-root --only main

COPY ./ ${LAMBDA_TASK_ROOT}/

CMD ["src/main.handler"]