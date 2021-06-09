FROM python:3.7-slim

WORKDIR /repo
COPY ./ /repo

RUN chmod -R 755 /repo
# Install internal dependencies
RUN pip install -U pip
RUN pip -q install pylint==2.6.0
RUN pip -q install yamllint
RUN pip install --user -r /repo/requirements.txt
