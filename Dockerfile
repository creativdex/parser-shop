FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update && apt-get -y install

COPY . .
RUN pip install -r requirements.txt

RUN pip install uvicorn[standard]

CMD uvicorn server:app --host 0.0.0.0 --port 8000 --workers 2 --loop uvloop
EXPOSE 8000