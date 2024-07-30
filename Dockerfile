FROM python:3.9-slim

RUN mkdir -p /usr/src/model
RUN mkdir -p /usr/src/db
RUN mkdir -p /usr/src/tests

WORKDIR /usr/src/

# Install build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY app.py requirements.txt serve.py ./

COPY ./db ./db
COPY ./model ./model
COPY ./tests ./tests

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "serve:app", "--host", "0.0.0.0", "--port", "8000"]
