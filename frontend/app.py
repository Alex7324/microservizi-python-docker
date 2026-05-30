import streamlit as st
import requests

# Titolo della pagina
st.set_page_config(page_title="Dashboard Aziendale", layout="wide")
st.title("💻 Dashboard Gestione Aziendale")

# Creiamo due colonne visive
col1, col2 = st.columns(2)

with col1:
    st.header("👤 Aggiungi Nuovo Utente")
    nuovo_nome = st.text_input("Nome Utente")
    nuovo_ruolo = st.text_input("Ruolo (es. Sviluppatore)")
    
    if st.button("Salva Utente"):
        if nuovo_nome and nuovo_ruolo:
            # Chiamata POST all'API Utenti (usando la rete interna di Docker!)
            risposta = requests.post(
                "http://api-utenti:8000/utenti/", 
                json={"nome": nuovo_nome, "ruolo": nuovo_ruolo}
            )
            if risposta.status_code == 200:
                st.success(f"Utente salvato! ID assegnato: {risposta.json()['nuovo_id']}")
            else:
                st.error("Errore durante il salvataggio")
        else:
            st.warning("Compila tutti i campi!")

with col2:
    st.header("📦 Cerca Ordine")
    id_ordine = st.number_input("Inserisci ID Ordine (es. 99)", min_value=1, step=1)
    
    if st.button("Cerca"):
        # Chiamata GET all'API Ordini
        risposta = requests.get(f"http://api-ordini:8000/ordini/{id_ordine}")
        
        if risposta.status_code == 200:
            dati = risposta.json()
            st.json(dati) # Mostra il JSON in modo elegante e formattato
        else:
            st.error("Ordine non trovato")

st.markdown("---")

st.header("📋 Lista di Tutti gli Utenti")

# Un bottone per ricaricare la lista
if st.button("Aggiorna Lista Utenti"):
    risposta = requests.get("http://api-utenti:8000/utenti/")
    
    if risposta.status_code == 200:
        utenti = risposta.json()
        if utenti:
            st.dataframe(utenti, use_container_width=True)
        else:
            st.info("Nessun utente presente nel database. Aggiungine uno sopra!")
    else:
        st.error("Errore nel recupero degli utenti")