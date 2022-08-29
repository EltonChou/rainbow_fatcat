FROM python:3.10-slim

ENV PYTHONPATH "${PYTHONPATH}:/workspace"

WORKDIR /workspace

COPY requirements.txt .
COPY rainbow_fatcat rainbow_fatcat/

RUN pip install -r requirements.txt

CMD ["python", "rainbow_fatcat/app.py"]
