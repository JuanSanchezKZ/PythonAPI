FROM python:3.8.5-alpine

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . /code

WORKDIR /code

COPY ./entrypoint.sh /code/
ENTRYPOINT ["sh", "entrypoint.sh"]



