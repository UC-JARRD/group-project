# iFireTracker Model Documentation

## Overview

The iFireTracker Model is a Python-based application that generates a map displaying fire risk levels for different land use areas around Christchurch, New Zealand. The risk levels are calculated based on weather station data and land use information.

Original Data Sources:
- Land use information: LUCAS NZ land use map (https://data.mfe.govt.nz/layer/52375-lucas-nz-land-use-map-1990-2008-2012-2016-v011/)

- Weather station data: NIWA Fire Weather (https://fireweather.niwa.co.nz/region/Canterbury)

The application consists of the following main components:

1. **Data Loading**: The `load_data.py` module loads the required data from CSV files and merges them into a single dataset.
2. **Data Processing**: The `process_data.py` module assigns fire risk levels to each land use area based on the weather station data and land type.
3. **Map Generation**: The `create_map.py` module generates an HTML file containing an interactive map with layers displaying the fire risk levels for today, tomorrow, and five days from the current date.
4. **Land Use Area Generation**: The `generate_land_use_areas_per_station.py` module generates a CSV file containing the land use areas grouped by the closest weather station and land type.
5. **Main Execution**: The `main.py` module orchestrates the execution of the other modules and handles logging.


## File Structure

The project follows the following file structure:

```
src/
├── iFireTrackerModel/
│   ├── model/
│   │   ├── data/
│   │   │   ├── input/
│   │   │   │   ├── canterbury_weather_stations.csv
│   │   │   │   ├── fire_risk.csv
│   │   │   │   ├── lucas-nz-land-use-map-1990-2008-2012-2016-v011.shx
│   │   │   │   └── merged/
│   │   │   │       └── land_use_areas_per_station.csv
│   │   │   └── output/
│   │   │       ├── csv/
│   │   │       │   └── fire_risk_per_land_use_area.csv
│   │   │       ├── html/
│   │   │       │   └── fire_risk_map.html
│   │   │       └── logs/
│   │   │           └── main_execution.log
│   │   ├── create_map.py
│   │   ├── generate_land_use_areas_per_station.py
│   │   ├── load_data.py
│   │   ├── main.py
│   │   └── process_data.py
```

## Module Documentation

### `load_data.py`

This module loads the weather station data and fire risk data from CSV files and merges them into a single DataFrame.

#### Functions

- `load_data()`: Loads the weather station coordinates and fire risk data, merges them, and loads the land use data. Returns two DataFrames: `station_fire_risk` and `land_use_data`.

### `process_data.py`

This module assigns fire risk levels to each land use area based on the weather station data and land type.

#### Functions

- `process_data(station_fire_risk, land_use_data)`: Takes two DataFrames as input: `station_fire_risk` and `land_use_data`. Assigns fire risk levels for today, tomorrow, and five days from the current date to each land use area based on the closest weather station and land type. Returns the updated `land_use_data` DataFrame.

### `create_map.py`

This module generates an HTML file containing an interactive map with layers displaying the fire risk levels for today, tomorrow, and five days from the current date.

#### Constants

- `CENTRE_LAT` and `CENTRE_LON`: Latitude and longitude of the center point for the map (in this case, Christchurch city).
- `RISK_COLORS` and `RISK_WORDS`: Dictionaries mapping risk levels to colors and words, respectively based on the Fire Risk off the NIWA website(https://fireweather.niwa.co.nz/region/Canterbury).

#### Functions

- `add_geojson_layer(map_layer, risk_day, tooltip_text, geometry, risk_level)`: Adds a GeoJSON layer to the provided map layer with the specified risk day, tooltip text, geometry, and risk level.
- `create_map(fire_risk_per_land_use_area)`: Creates an HTML file (`fire_risk_map.html`) containing an interactive map with layers displaying the fire risk levels for today, tomorrow, and in five days from the current date. The map is centered on Christchurch city and includes a legend for the risk levels.

### `generate_land_use_areas_per_station.py`

This module generates a CSV file containing the land use areas grouped by the closest weather station and land type.

#### Functions

- `generate_land_use_areas_per_station()`: Loads the weather station location data and the LUCAS NZ land use map data. Determines the land type for each polygon in the land use data and finds the closest weather station for each polygon. Groups the polygons by closest station and land type, merges the geometries in each group, and saves the resulting DataFrame to a CSV file (`land_use_areas_per_station.csv`).
- 

### `main.py`

This module orchestrates the execution of the other modules and handles logging.


#### Functions

- `main()`: Loads the data using `load_data.load_data()`, processes the data using `process_data.process_data()`, saves the processed data to a CSV file, and creates the map using `create_map.create_map()`.
- 

## Usage

To run the iFireTracker Model application, follow these steps:

1. Ensure that you have the required dependencies installed from requirements.txt
2. Navigate to the project directory (`src/iFireTrackerModel/model/`).
3. Run the `main.py` script:

```
python main.py
```

This will execute the application, generating a CSV file (`fire_risk_per_land_use_area.csv`) containing the processed data and an HTML file (`fire_risk_map.html`) with an interactive map displaying the fire risk levels.

Note: The application assumes that the required input files (`canterbury_weather_stations.csv`, `fire_risk.csv`, and `lucas-nz-land-use-map-1990-2008-2012-2016-v011.shx`) are present in the `src/iFireTrackerModel/model/data/input/` directory.


## Logging

The application uses the Python `logging` module to log important events, warnings, and errors during execution. The logs are written to the `main_execution.log` file located in the `src/iFireTrackerModel/model/logs/` directory.


## Schedule tasks using Cron on EC2

To periodically update prediction files, they need to be runned the model and sent to MySQL database, S3 file server and Web server. For this, Cron is used with a schedule to run script every hour.

1. Grant file execution rights to script.

`chmod +x get_s3.sh`

2. Using the command `crontab -e` add the following entry to run the script every hour

`0 */1 * * * /home/ubuntu/iFireTrackerModel/run_model.sh`

3. Check if the entry was successfully added to the Cron table, run the command `crontab -l`

4. Restart Cron and check the status

```
sudo systemctl stop cron
sudo systemctl start cron
sudo systemctl enable cron
sudo systemctl status cron
```

## Dependencies

The iFireTracker Model application relies on the following Python libraries:

- pandas
- geopandas
- folium
- shapely

Make sure to install these dependencies before running the application.

## Future Improvements

Here are some potential areas for future improvements:

- Implement error handling, logging and data validation for input files.
- Enhance the map visualization with additional features, such as interactive legends and filtering options.
- Widen the area of map to all of Canterbury or New Zealand as a whole.
- Implement automated testing for the different modules.
- Explore parallelization or optimization techniques to improve performance for larger datasets.