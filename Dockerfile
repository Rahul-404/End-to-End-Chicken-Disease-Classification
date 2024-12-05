FROM python:3.9-slim-buster

RUN apt upadte -y && install awscli -y

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "app.py"]