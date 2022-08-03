FROM python:3.9-slim
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache -r requirements.txt
COPY . /app
WORKDIR /app

CMD ["gunicorn", "app:server", "0.0.0.0:80"]