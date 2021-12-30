# pull official base image
FROM python:3.10-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apk update \
    && apk add --virtual build-essential gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt


# copy project
COPY . .

RUN python manage.py collectstatic --noinput

RUN adduser -D myuser
USER root
RUN chown myuser /app
RUN chown myuser /app/db.sqlite3
USER myuser
#chown myuser db.sqlite3 
 
CMD gunicorn blog_backend.wsgi:application --bind 0.0.0.0:$PORT
