# syntax=docker/dockerfile:1

FROM python:3.9
COPY . /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]