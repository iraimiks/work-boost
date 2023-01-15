FROM python:3

WORKDIR /python_docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python run.py db init
RUN python run.py db migrate -m "Initial migration."
RUN python run.py db upgrade

CMD ["python", "./run.py"]