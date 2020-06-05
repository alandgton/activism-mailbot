FROM python:3.7-slim

WORKDIR /usr/app/src

COPY . .

RUN pip install -r requirements.txt

CMD tail -f /dev/null
