FROM python:3.12-slim-bullseye
WORKDIR /survey

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python","-m","flask","--app","main","run","--host=0.0.0.0"]