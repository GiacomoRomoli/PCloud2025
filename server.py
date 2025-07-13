from flask import Flask,request,redirect,url_for
import json

from google.cloud import firestore

app = Flask(__name__)

@app.route('/graph', methods=['GET'])
def graph():
    return redirect(url_for('static', filename='sito.html'))


@app.route('/sensors',methods=['GET']) #prendo i valori delle racolte presenti nel db e li restituisco in questo url
def sensors():
    db = "pcloud2025"
    db = firestore.Client.from_service_account_json('credentials.json', database=db)
    l = []
    for i in db.collections():
        l.append(i.id) #vado ad appendere gli id, quindi i nomi dei sensori, quindi i nomi delle città
    return json.dumps(l), 200


@app.route('/sensors/<s>',methods=['POST'])
def add_data(s):
    db = "test"
    db = firestore.Client.from_service_account_json('credentials.json', database=db)
    date = request.values['date']
    road_name = request.values['road name']
    traffic_volume = float(request.values['traffic volume'])
    average_speed = float(request.values['average speed'])
    travel_time_index = float(request.values['travel time index'])
    congestion_level = float(request.values['congestion level'])
    road_capacity_utilization = float(request.values['road capacity utilization'])
    incident_reports = float(request.values['incident reports'])
    environmental_impact = float(request.values['eviromental impact'])
    public_transport_usage = float(request.values['public transport usage'])
    traffic_signal_compliance = float(request.values['traffic signal compliance'])
    parking_usage = float(request.values['parking usage'])
    pedestran_and_cyclist_count = float(request.values['pedestrian and cyclist count'])
    weather_conditions =request.values['weather conditions']
    roadwork_and_construction_activity = request.values['roadwork and construction activity']
    latitude = float(request.values['latitude'])
    longitude = float(request.values['longitude'])
    doc_ref = db.collection(s).document(date) #faccio riferimento ad un documento.
    doc_ref.set({'date': date,
                 'road name': road_name,
                 'traffic volume': traffic_volume,
                 'average speed': average_speed,
                 'travel time index': travel_time_index,
                 'congestion level': congestion_level,
                 'road capacity utilization': road_capacity_utilization,
                 'incident reports': incident_reports,
                 'eviromental impact': environmental_impact,
                 'public transport usage': public_transport_usage,
                 'traffic signal compliance': traffic_signal_compliance,
                 'parking usage': parking_usage,
                 'pedestrian and cyclist count': pedestran_and_cyclist_count,
                 'weather conditions': weather_conditions,
                 'roadwork and construction activity': roadwork_and_construction_activity,
                 'latitude': latitude,
                 'longitude': longitude}) #creo un nuovo documento con questi valori
    return 'ok',200

@app.route('/sensors/<s>',methods=['GET'])
def get_data(s):
    db = "test"
    db = firestore.Client.from_service_account_json('credentials.json', database=db)
    l = []
    for i in db.collections():
        l.append(i.id)
    if s in l:
        r = []
        doc_ref = db.collection(s) #faccio riferimento alla collection s
        for i in range(0, len(doc_ref.get())): #col get ottengo in formato di lista gli identificativi dei documenti, ossia le rilevazioni che fa il sensore s
            r.append(doc_ref.get()[i].to_dict()) #faccio riferimento al documento i-esimo e appendo i valori di questo documento
        return json.dumps(r), 200
    else:
        return 'sensor not found',404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) #host = '0.0.0.0' vuol dire che possono accedervi tutti, anche utenti esterni che non usano questo computer; la porta è 80. Quindi per accedere al server sul computer dovrò digitare l'url:"localhost:80" o solo "localhost" (questo nel caso in cui un endpoint è solo "\")
