FROM python:3.10-slim AS base

# don't buffer python stdout or stderr so that docker logs shows output immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/python-logging-example
COPY main.py main.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
CMD ["python", "main.py"]