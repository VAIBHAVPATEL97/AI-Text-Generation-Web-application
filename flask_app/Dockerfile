FROM python:3.6.13

WORKDIR /home/uavproject/Desktop/Docker-gpt2/flask_app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
