from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/ordini/{order_id}")
def get_ordine(order_id: int):
    # Non usiamo 'localhost', ma il nome del container ('api-utenti')
    url_servizio_utenti = "http://api-utenti:8000/utenti/1"
    
    try:
        risposta = requests.get(url_servizio_utenti)
        dati_utente = risposta.json()
    except:
        dati_utente = {"errore": "Servizio Utenti offline"}

    return {
        "id_ordine": order_id,
        "prodotto": "Tastiera Meccanica",
        "cliente": dati_utente
    }