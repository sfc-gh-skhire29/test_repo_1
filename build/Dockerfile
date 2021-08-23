FROM python:3.7-slim

WORKDIR /repo
COPY ./ /repo

RUN chmod -R 755 /repo
# Install internal dependencies
RUN pip install -U pip
RUN pip install jsonschema
RUN pip install fastjsonschema