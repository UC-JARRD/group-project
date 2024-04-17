import geopandas as gpd
import pandas as pd

def load_data():
    # Load weather station data
    weather_stations_coords = pd.read_csv('src/models/model1/data/canterbury_weather_stations.csv') # coordinates of each station
    fire_risk = pd.read_csv('src/models/model1/data/fire_risk.csv') # fire risk at each station (will come from database eventually)

    # Merge the datasets on the 'station_name' column
    station_fire_risk = pd.merge(weather_stations_coords, fire_risk, on='station_name')

    # Load LUCAS NZ land use map data (shapefile)
    land_use_data = gpd.read_file('src/models/model1/data/lucas-nz-land-use-map-1990-2008-2012-2016-v011.shx') # Can reduce row numbers using e.g. rows=1000
    # Set the coordinate system
    land_use_data = land_use_data.to_crs("EPSG:4326")

    # Drop all columns except 'geometry', 'land_type', and 'fire_risk'
    columns_to_keep = ['geometry', 'LUCID_2016', 'LUCNA_2016']
    land_use_data = land_use_data[columns_to_keep]

    return station_fire_risk, land_use_data