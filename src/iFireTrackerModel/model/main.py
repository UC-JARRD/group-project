import logging
import load_data
import process_data
import create_map
import datetime
import os
import sys
config_path = f'{os.path.expandvars('$MODEL_SERVER_PATH')}/config/'
sys.path.append(config_path)
import config

LOG_PATH = config.log_path
OUTPUT_FIRE_RISK_LAND_USE_PATH = config.csv_output_local_path

# Configure logging
logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
# Get today's date
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def main():
    logging.info("Starting main function...")

    try:
        # Load the data
        logging.info("Loading data...")
        station_fire_risk, land_use_data = load_data.load_data()
        logging.info('Data loaded successfully.')
        print(f'{time} Data loaded successfully.')

        # Process the data
        logging.info("Processing data...")
        fire_risk_per_land_use_area = process_data.process_data(station_fire_risk, land_use_data)
        logging.info('Data processed successfully.')
        print(f'{time} Data processed successfully.')

        # Save fire_risk_per_polygon DataFrame to CSV
        logging.info("Saving data...")
        fire_risk_per_land_use_area.to_csv(OUTPUT_FIRE_RISK_LAND_USE_PATH, index=False)
        logging.info('Data saved to output CSV file successfully.')
        print(f'{time} Data saved successfully.')

        # Create the map
        logging.info("Creating map...")
        create_map.create_map(fire_risk_per_land_use_area)
        logging.info('Map created successfully.')
        print(f'{time} Map created successfully.')

    except Exception as e:
        logging.error(f"Error in main function: {str(e)}")
        print(f'{time} Error in main function: {str(e)}')
        raise

if __name__ == "__main__":
    main()