FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code/

COPY requirements/google-chrome-stable_current_amd64.deb /code/
COPY requirements/requirements.txt /code/requirements.txt
COPY requirements/chromedriver /code/requirements/chromedriver

RUN pip install -r /code/requirements.txt

COPY . /code/

RUN apt-get update

# Install Chromium
RUN apt update && apt install chromium -y
RUN dpkg -i google-chrome-stable_current_amd64.deb

# install dependencies
RUN pip install --upgrade pip
