FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

# Install the dependencies
#
