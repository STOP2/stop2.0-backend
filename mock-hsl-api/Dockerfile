FROM python:3.5.2

RUN apt-get install libpq-dev

ADD requirements.txt /

RUN pip install -r /requirements.txt

EXPOSE 11111

CMD python app.py

ADD . /
