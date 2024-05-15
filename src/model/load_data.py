import pandas as pd

def load_data():
    # Load weather station data
    weather_stations_coords = pd.read_csv('src/models/model1/data/canterbury_weather_stations.csv') # coordinates of each station
    fire_risk = pd.read_csv('src/models/model1/data/fire_risk.csv') # fire risk at each station (will come from database eventually)

    # Merge the datasets on the 'station_name' column
    station_fire_risk = pd.merge(weather_stations_coords, fire_risk, on='station_name')

    # Load land_use_data
    land_use_data = pd.read_csv('src/models/model1/data/land_use_areas_per_station.csv')

    return station_fire_risk, land_use_data