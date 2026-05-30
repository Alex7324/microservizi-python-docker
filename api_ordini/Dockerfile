FROM python:3.10-slim

WORKDIR /app


COPY requirements.txt .
RUN pip install -r requirements.txt


COPY . .

# Avvia l'app FastAPI usando Uvicorn, esponendo la porta 8000 per le richieste HTTP
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]