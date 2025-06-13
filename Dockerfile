FROM python:3.10-slim

RUN useradd -m appuser
WORKDIR /app
COPY app /app

RUN pip install --no-cache-dir -r requirements.txt
USER appuser

EXPOSE 5000
CMD ["python", "main.py"]
