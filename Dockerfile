FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /src .

RUN ls /code

RUN python -m py_compile /code/calc.py

