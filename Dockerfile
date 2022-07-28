FROM python:3.7

WORKDIR /app

COPY calculator.py app.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENTRYPOINT ["python3","app.py"]
