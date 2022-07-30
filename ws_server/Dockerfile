FROM python:3.9-slim
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache -r requirements.txt
COPY . /app
WORKDIR /app

CMD ["python3", "server.py"]