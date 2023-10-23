FROM python:latest

WORKDIR /app

COPY ./ ./

RUN pip install --upgrade pip 

COPY . ./

