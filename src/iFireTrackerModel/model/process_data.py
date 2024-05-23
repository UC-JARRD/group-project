import logging
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

LOG_PATH = './logs/main_execution.log'

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOG_PATH)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

def process_data(station_fire_risk, land_use_data):
    logging.info("[process_data.py] Processing data...")
    # Assign fire risk to each polygon for today, tomorrow, and five days
    def assign_fire_risk(row, day):
        try:
            station = station_fire_risk.loc[row['closest_station']]
            land_type = row['land_type']
            risk_column = f"{day}_{land_type}"
            if land_type == 'water':
                return 0  # Assign 0 risk for water
            return station[risk_column]
        except KeyError:
            logging.warning(f"[process_data.py] No data found for {row['closest_station']} for {day}")
            return None
        except Exception as e:
            logging.error(f"[process_data.py] Error processing data: {str(e)}")
            raise

    try:
        land_use_data['fire_risk_today'] = land_use_data.apply(assign_fire_risk, args=('today',), axis=1)
        land_use_data['fire_risk_tomorrow'] = land_use_data.apply(assign_fire_risk, args=('tomorrow',), axis=1)
        land_use_data['fire_risk_five_days'] = land_use_data.apply(assign_fire_risk, args=('five_days',), axis=1)
        logging.info("[process_data.py] Data processed successfully.")
    except Exception as e:
        logging.error(f"[process_data.py] Error processing data: {str(e)}")
        raise
    
    return land_use_data
