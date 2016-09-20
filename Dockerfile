FROM python:3.5.2-alpine

ADD . .

RUN pip install -r requirements.txt

WORKDIR "src"

EXPOSE 5000

CMD python stop.py
