import logging
import pandas as pd
import datetime
import os

LOG_PATH = '../logs/model_execution.log'
INPUT_WEATHER_STATIONS_PATH = './data/input/canterbury_weather_stations.csv'
MERGED_LAND_USE_STATIONS_PATH = './data/input/merged/land_use_areas_per_station.csv'
INPUT_FIRE_RISK_PATH_PREFIX = './data/input/everyday_data/'

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(LOG_PATH)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

def get_today_fire_risk_path():
    # Get today's date
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    # Construct the file name
    fire_risk_filename = f"{today}_fire_risk.csv"
    # Construct the full file path
    fire_risk_filepath = os.path.join(INPUT_FIRE_RISK_PATH_PREFIX, fire_risk_filename)
    return fire_risk_filepath

def load_data():
    logging.info("[load_data.py] Loading weather station data...")

    # Load weather station data
    try:
        weather_stations_coords = pd.read_csv(INPUT_WEATHER_STATIONS_PATH) # coordinates of each station
        logging.info("[load_data.py] Weather station data loaded successfully.")
    except FileNotFoundError:
        logging.error("[load_data.py] Failed to load weather station data. File not found.")
        raise

    # Get today's fire risk file path
    fire_risk_filepath = get_today_fire_risk_path()
    
    try:
        # Load fire risk data
        fire_risk = pd.read_csv(fire_risk_filepath)
        logging.info(f"[load_data.py] Fire risk data for today ({fire_risk_filepath}) loaded successfully.")
    except FileNotFoundError:
        logging.error(f"[load_data.py] Failed to load fire risk data for today ({fire_risk_filepath}). File not found.")
        raise


    # Merge the datasets on the 'station_name' column
    logging.info("[load_data.py] Merging weather station data...")
    try:
        station_fire_risk = pd.merge(weather_stations_coords, fire_risk, on='station_name')
        logging.info("[load_data.py] Datasets merged successfully.")
    except Exception as e:
        logging.error(f"[load_data.py] Failed to merge datasets: {str(e)}")
        raise

    logging.info("[load_data.py] Loading land use data...")
    # Load land_use_data
    try:
        land_use_data = pd.read_csv(MERGED_LAND_USE_STATIONS_PATH)
        logging.info("[load_data.py] Land use data loaded successfully.")
    except FileNotFoundError:
        logging.error("[load_data.py] Failed to load land use data. File not found.")
        raise

    return station_fire_risk, land_use_data