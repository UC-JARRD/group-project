import geopandas as gpd
from shapely.geometry import Point

def process_data(weather_data, land_use_data):
    # Determine the land type for each polygon
    land_use_mappings = {
        71: 'forest', # Natural Forest
        72: 'forest', # Planted Forest - Pre 1990
        73: 'forest', # Post 1989 Forest
        74: 'scrub',  # Grassland - With woody biomass
        75: 'grass',  # Grassland - High producing
        76: 'grass',  # Grassland - Low producing
        77: 'grass',  # Cropland - Orchards and vineyards (perennial)
        78: 'grass',  # Cropland - Annual
        79: 'grass',  # Wetland - Open water
        80: 'grass',  # Wetland - Vegetated non forest
        81: 'grass',  # Settlements or built-up area
        82: 'grass'   # Other
    }
    
    land_use_data['land_type'] = land_use_data['LUCID_2016'].map(land_use_mappings)

    # Convert weather station coordinates to GeoDataFrame
    geometry = [Point(xy) for xy in zip(weather_data['longitude'], weather_data['latitude'])]
    weather_stations = gpd.GeoDataFrame(weather_data, geometry=geometry)

    # Find the closest weather station for each polygon
    land_use_data['closest_station'] = land_use_data.geometry.apply(lambda x: weather_stations.distance(x).idxmin())
    # Get the name of the closest station for each polygon
    land_use_data['closest_station_name'] = land_use_data['closest_station'].apply(lambda x: weather_data.loc[x, 'station_name'])

    # Assign fire risk to each polygon
    def assign_fire_risk(row):
        station = weather_data.loc[row['closest_station']]
        land_type = row['land_type']
        return station[land_type]

    land_use_data['fire_risk'] = land_use_data.apply(assign_fire_risk, axis=1)

    return land_use_data