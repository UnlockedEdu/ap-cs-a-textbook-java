FROM python:latest

COPY requirements.txt /requirements.txt

WORKDIR /data

RUN pip3 install -r /requirements.txt

CMD ["mkdocs", "serve", "-a", "0.0.0.0:8000"]
