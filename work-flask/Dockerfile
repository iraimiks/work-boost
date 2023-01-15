FROM python:3

WORKDIR /python_docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN flask --app run.py db init
RUN flask --app run.py db migrate -m "Initial migration."
RUN flask --app run.py db upgrade

CMD ["python", "./run.py"]