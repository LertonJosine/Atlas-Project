FROM python:3

# set enviroments variables

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1


WORKDIR /Atlas

COPY ./requirements.txt .

RUN pip install -r requirements.txt 

COPY . .
