FROM python:3.10.7-slim-bullseye

RUN pip install --no-cache-dir Flask==2.2.2 gunicorn==20.1.0

WORKDIR /app
COPY gunicorn_conf.py /gunicorn_conf.py
COPY api.py .

RUN useradd user
USER user
CMD ["gunicorn", "-c", "/gunicorn_conf.py"]
