FROM python:3.8-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV CONFIG_NAME=DevelopmentConfig

RUN chmod +x prestart.sh
ENTRYPOINT ["bash", "prestart.sh"]

EXPOSE 8000
CMD python app.py