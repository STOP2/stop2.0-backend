FROM python:3.5.2

RUN apt-get install libpq-dev

ADD requirements.txt /

RUN pip install -r /requirements.txt

WORKDIR "/src"

EXPOSE 5000

CMD python stop.py

ADD . /
