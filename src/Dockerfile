FROM python:3.9-slim
LABEL maintainer="Julio Cesar <julio@blackdevs.com.br>"

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r \
    requirements.txt --no-cache-dir
COPY . .

RUN pip freeze

CMD ["python", "-u", "main.py"]
