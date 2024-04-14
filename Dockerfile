FROM python:3.11

WORKDIR /app
RUN apt-get update && apt-get upgrade -y && apt-get install -y chromium-driver chromium pulseaudio && pip install selenium
COPY main.py /app/
CMD ["python", "main.py"]
