import geopandas as gpd
from shapely.geometry import Point

def process_data(station_fire_risk, land_use_data):
    # Determine the land type for each polygon in land_use_data
    land_use_mappings = {
        71: 'forest', # Natural Forest
        72: 'forest', # Planted Forest - Pre 1990
        73: 'forest', # Post 1989 Forest
        74: 'scrub',  # Grassland - With woody biomass
        75: 'grass',  # Grassland - High producing
        76: 'grass',  # Grassland - Low producing
        77: 'grass',  # Cropland - Orchards and vineyards (perennial)
        78: 'grass',  # Cropland - Annual
        79: 'water',  # Wetland - Open water 
        80: 'grass',  # Wetland - Vegetated non forest
        81: 'grass',  # Settlements or built-up area
        82: 'grass'   # Other
    }
    
    land_use_data['land_type'] = land_use_data['LUCID_2016'].map(land_use_mappings)

    # Convert weather station coordinates to GeoDataFrame
    geometry = [Point(xy) for xy in zip(station_fire_risk['longitude'], station_fire_risk['latitude'])]
    weather_stations = gpd.GeoDataFrame(station_fire_risk, geometry=geometry)

    # Find the closest weather station for each polygon
    land_use_data['closest_station'] = land_use_data.geometry.apply(lambda x: weather_stations.geometry.distance(x).idxmin())

    # Get the name of the closest station for each polygon
    land_use_data['closest_station_name'] = land_use_data['closest_station'].apply(lambda x: station_fire_risk.loc[x, 'station_name'])
    
    # Assign fire risk to each polygon for today, tomorrow, and five days
    def assign_fire_risk(row, day):
        station = station_fire_risk.loc[row['closest_station']]
        land_type = row['land_type']
        risk_column = f"{day}_{land_type}"
        if land_type == 'water':
            return 0  # Assign 0 risk for water
        return station[risk_column]

    land_use_data['fire_risk_today'] = land_use_data.apply(assign_fire_risk, args=('today',), axis=1)
    land_use_data['fire_risk_tomorrow'] = land_use_data.apply(assign_fire_risk, args=('tomorrow',), axis=1)
    land_use_data['fire_risk_five_days'] = land_use_data.apply(assign_fire_risk, args=('five_days',), axis=1)

    return land_use_data