FROM python:3.5.2

ADD . .

RUN apt-get install libpq-dev

RUN pip install -r requirements.txt

WORKDIR "src"

EXPOSE 5000

CMD ./stop.sh
