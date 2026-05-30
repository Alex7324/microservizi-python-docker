from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import time
import os 

app = FastAPI()

def get_db_connection():
    retries = 5
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host="db", 
                database=os.getenv("DB_NOME"),       
                user=os.getenv("DB_UTENTE"),         
                password=os.getenv("DB_PASSWORD")    
            )
            return conn
        except psycopg2.OperationalError:
            time.sleep(2)
            retries -= 1
    raise Exception("Database irraggiungibile")

@app.on_event("startup")
def startup_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utenti (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(50),
            ruolo VARCHAR(50)
        );
    """)
    cursor.execute("SELECT COUNT(*) FROM utenti;")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO utenti (id, nome, ruolo) VALUES (1, 'Alessandro', 'Ingegnere Ponte');")
    conn.commit()
    cursor.close()
    conn.close()

class NuovoUtente(BaseModel):
    nome: str
    ruolo: str

# 4. Rotta GET (Lettura)
@app.get("/utenti/{user_id}")
def get_utente(user_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, ruolo FROM utenti WHERE id = %s", (user_id,))
    utente = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if utente:
        return {"nome": utente[0], "ruolo": utente[1]}
    return {"errore": "Utente non trovato nel Database"}

@app.post("/utenti/")
def crea_utente(utente: NuovoUtente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO utenti (nome, ruolo) VALUES (%s, %s) RETURNING id;",
        (utente.nome, utente.ruolo)
    )
    nuovo_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return {"messaggio": "Utente creato con successo!", "nuovo_id": nuovo_id}