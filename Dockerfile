FROM python:3.9-slim

WORKDIR /app

COPY app/ .

RUN pip install flask

ENV APP_VERSION=blue

CMD ["python", "main.py"]