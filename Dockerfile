FROM python:3.5.2

ADD . .

RUN pip install -r requirements.txt

WORKDIR "src"

EXPOSE 5000

CMD python stop.py