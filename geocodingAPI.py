import pandas as pd
import requests
import time

API_KEY = "AIzaSyBAikOcOKX05WDHGgq38uCC323oogYQPWY"

#Leggo il file
df = pd.read_csv("Banglore_traffic_Dataset.csv")

#Colonne corrette
area_col = "Area Name"
road_col = "Road/Intersection Name"

#Questa funzione prende un’area e una strada, costruisce un indirizzo, invia una richiesta all’API di Google e riceve in risposta la latitudine e la longitudine.
def geocode_address(area, road):
    address = f"{road}, {area}, Bangalore, India" #costruisco una stringa con l'indirizzo da cercare con google geocoding.
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}" #costruisco l'URL dell'API di Google Geocoding
    response = requests.get(url) #ottengo una risposta json con i dati corrispondeti all'url
    if response.status_code == 200:
        data = response.json() #converto la risposta in un dizionario Python, partendo dal JSON ricevuto. Il dizionario contiene le latitudini e longitudini
        if data['status'] == 'OK': #verifico che l’API abbia trovato un risultato valido
            location = data['results'][0]['geometry']['location'] #restituisce una doppia coppia chiave valore con lat e long. Esempio: {"lat": 12.935192, "lng": 77.624480}
            return location['lat'], location['lng']
    return None, None

latitudes = []
longitudes = []

for indice, riga in df.iterrows(): #itero facendomi restituire ogni riga come una sorta di dizionario composta da coppie chiave valore, dove la chiave è il nome della colonna.
    area = riga[area_col] #prendo il valore dell'area che sta sotto la colonna Area Name
    road = riga[road_col]
    lat, lng = geocode_address(area, road)
    print(f"[{indice}] {area}, {road}, lat: {lat}, lng: {lng}")
    latitudes.append(lat)
    longitudes.append(lng)
    time.sleep(0.1) #per non sovraccaricare l’API lo faccio ogni 0.1 secondi

df["Latitude"] = latitudes
df["Longitude"] = longitudes

#Salvo in nuovo file per evitare di sovrascrivere
df.to_csv("Banglore_traffic_Dataset_geocoded.csv", index=False)
print("File salvato con coordinate.")