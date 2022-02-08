#How to run?
#1. install "docker" on your computer
#2. Type in terminal: docker build . -t <name_image> (. = from current directory)
#3. After installation type in terminal: docker run -it -p 8000:8000 <name_image>

FROM python:3.8-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD uvicorn main:app --host=0.0.0.0 --port=8000