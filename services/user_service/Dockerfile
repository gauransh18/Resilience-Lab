FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

# FROM golang:1.17-alpine

# WORKDIR /app

# COPY . .

# RUN go build -o main

# CMD ["./main"]
