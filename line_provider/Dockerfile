FROM python:3.10
WORKDIR /
RUN pip install --no-cache-dir --upgrade fastapi uvicorn aio_pika python-dotenv
COPY app.py app.py
COPY event_publisher.py event_publisher.py
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
