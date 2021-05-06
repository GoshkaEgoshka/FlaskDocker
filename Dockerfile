FROM python:3

RUN apt-get update && apt-get upgrade -y
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY web ./web
EXPOSE 5000

CMD python ./web/main.py