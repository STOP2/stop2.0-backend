FROM python:3.5.2

ADD . .

RUN apt-get install libpq-dev

RUN pip install -r requirements.txt

EXPOSE 11111

CMD python app.py
