FROM python:3.7.5

ADD app.py / 

ADD model.h5 /

ADD requirements.txt /

ADD texts.p /

RUN pip install -r requirements.txt

ENTRYPOINT flask run --without-threads -h 0.0.0.0 -p 1313
