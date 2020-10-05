FROM python:3.8

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /src .

RUN python -m py_compile /code/src/calc.py

