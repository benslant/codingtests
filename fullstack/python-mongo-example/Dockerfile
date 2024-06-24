FROM python:3.12.4-alpine

WORKDIR /app

#Freeze the poetry requirements to PIP requirements list
RUN pip freeze > requirements.txt

COPY