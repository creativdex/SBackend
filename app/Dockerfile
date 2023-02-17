FROM python:3.11-slim-bullseye

ENV PYTHONUNBUFFERED 1
WORKDIR /build

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install uvicorn[standard]

COPY alembic alembic
COPY app app
COPY alembic.ini .
COPY config.env .
COPY init.sh .

RUN addgroup --gid 1001 --system uvicorn && \
    adduser --gid 1001 --shell /bin/false --disabled-password --uid 1001 uvicorn

RUN chown -R uvicorn:uvicorn /build
CMD bash init.sh && \
    runuser -u uvicorn -- /venv/bin/uvicorn app.main:app --app-dir /build --host 0.0.0.0 --port 8000 --workers 2 --loop uvloop
EXPOSE 8000