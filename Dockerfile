FROM python:3.9 as builder

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD [ "python", "main.py" ]
