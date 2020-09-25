FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN ls -la /code

COPY /src .

RUN ls -la /code


