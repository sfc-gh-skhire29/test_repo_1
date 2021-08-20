FROM python:3.7-slim

WORKDIR /repo
COPY ./it_engineering/great_expectations /repo

RUN chmod -R 755 /repo
# Install internal dependencies
RUN pip install -U pip
RUN pip install jsonschema