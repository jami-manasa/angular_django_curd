FROM python:3
ENV PYTHONUNBUFFRED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt 
COPY ./app/
