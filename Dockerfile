FROM python:3

RUN apt-get update && apt-get upgrade -y
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY web ./web
COPY run.py ./
COPY migrations ./migrations
ENV FLASK_APP=web/app.py
ENV FLASK_RUN_HOST=0.0.0.0
EXPOSE 5000

CMD ["python", "run.py"] 