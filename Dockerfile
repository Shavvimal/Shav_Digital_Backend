# pull official base image
FROM python:3.8.12-slim

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN /usr/local/bin/python -m pip install --upgrade pip

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
EXPOSE 8000
# run gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]