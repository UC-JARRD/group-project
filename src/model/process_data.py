import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def process_data(station_fire_risk, land_use_data):

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