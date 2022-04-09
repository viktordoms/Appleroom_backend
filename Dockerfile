FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /BackEnd

WORKDIR /BackEnd

COPY requirements.txt /BackEnd
COPY .env /user/bin/

RUN  pip install --upgrade pip && pip install -r requirements.txt

CMD ./wait-for-it.sh  db:3306 --  python3 ./BackEnd/manage.py runserver 0.0.0.0:8091