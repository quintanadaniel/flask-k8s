FROM python:3.9.1-alpine

WORKDIR /app
COPY src/ /app
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \
            CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT [ "python", "app.py" ]

