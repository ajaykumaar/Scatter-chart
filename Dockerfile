from python:3.7-slim-stretch


WORKDIR /Scatter-chart

ADD . /Scatter-chart

RUN pip install -r requirements.txt


