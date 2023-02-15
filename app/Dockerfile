# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /code/app

# install psycopg2 dependencies
RUN apk update && apk add --no-cache gcc musl-dev python3-dev

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
