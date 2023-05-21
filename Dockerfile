FROM python:3.11.1-slim

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gettext \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install -r requirements.txt
