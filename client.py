from requests import get, post #librerie http per l'utilizzo di funzioni get e post
import time

base_url = 'http://localhost:80'
#base_url = '34.154.119.50'
with open('Banglore_traffic_Dataset_geocoded.csv') as f:
    for l in f.readlines()[1:]:
        date, area_name, road_name, traffic_volume, average_speed, travel_time_index, congestion_level, road_capacity_utilization, incident_reports, environmental_impact, public_transport_usage, traffic_signal_compliance, parking_usage, pedestran_and_cyclist_count, weather_conditions, roadwork_and_construction_activity, latitude, longitude = l.strip().split(',') #leggo solo i valori del csv
        print(date, area_name, road_name, traffic_volume, average_speed, travel_time_index, congestion_level, road_capacity_utilization, incident_reports, environmental_impact, public_transport_usage, traffic_signal_compliance, parking_usage, pedestran_and_cyclist_count, weather_conditions, roadwork_and_construction_activity, latitude, longitude)
        #area_name diventa il nome del sensore
        r = post(f'{base_url}/sensors/{area_name}',
                 data={'date': date,
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
                       'longitude': longitude}) #posto su questo url, questi valori
        #r = post(f'{base_url}/sensors/{area_name}', "\n")
        time.sleep(10) #posto i valori ogni 10 secondi