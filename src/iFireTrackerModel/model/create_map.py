import logging
import folium
from folium.plugins import Geocoder
from datetime import datetime, timedelta
from shapely.wkt import loads

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler('./logs/main_execution.log')
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)


# Constants
CENTRE_LAT = -43.525650  # Latitude of Christchurch city
CENTRE_LON = 172.639847  # Longitude of Christchurch city
RISK_COLORS = {0: 'transparent', 1: 'green', 2: 'blue', 3: 'yellow', 4: 'orange', 5: 'red'}
RISK_WORDS = {0: 'Water - No Risk', 1: 'Low', 2: 'Moderate', 3: 'High', 4: 'Very High', 5: 'Extreme'}

def add_geojson_layer(map_layer, risk_day, tooltip_text, geometry, risk_level):
    """
    Add GeoJson layer to the given map layer.
    """
    try:
        folium.GeoJson(
            geometry,
            style_function=lambda x, risk=risk_level: {
                'fillColor': RISK_COLORS.get(risk, 'gray'),
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.7
            },
            tooltip=folium.Tooltip(tooltip_text, sticky=True)
        ).add_to(map_layer)
        logging.info(f"[create_map.py] Added GeoJson layer for {tooltip_text}")
    except Exception as e:
        logging.error(f"[create_map.py] Failed to add GeoJson layer: {str(e)}")
        raise

def create_map(fire_risk_per_land_use_area):
    """
    Create a map with fire risk layers for today, tomorrow, and five days from now.
    """
    logging.info("[create_map.py] Creating fire risk map...")
    fire_risk_map = folium.Map(location=[CENTRE_LAT, CENTRE_LON], zoom_start=12)

    today_date = datetime.now().date()
    tomorrow_date = today_date + timedelta(days=1)
    five_days_date = today_date + timedelta(days=5)

    all_layers = folium.FeatureGroup()

    fire_risk_today_layer = folium.FeatureGroup(name=f'Fire Risk for {today_date}', overlay=True, control=True, show=True)
    # fire_risk_tomorrow_layer = folium.FeatureGroup(name=f'Fire Risk for {tomorrow_date}', overlay=True, control=True, show=False)
    # fire_risk_five_days_layer = folium.FeatureGroup(name=f'Fire Risk for {five_days_date}', overlay=True, control=True, show=False)

    fire_risk_per_land_use_area['geometry'] = fire_risk_per_land_use_area['merged_geometry'].apply(loads)

    for _, row in fire_risk_per_land_use_area.iterrows():
        closest_station = row['closest_station_name']
        land_type = row['land_type']
        geometry = row['geometry']

        risk_word_today = RISK_WORDS.get(row['fire_risk_today'], 'Unknown')
        tooltip_text_today = f"Land Category: {land_type.capitalize()}<br>Fire Risk: {risk_word_today}<br>Closest Station: {closest_station}"
        add_geojson_layer(fire_risk_today_layer, row['fire_risk_today'], tooltip_text_today, geometry, row['fire_risk_today'])

        # risk_word_tomorrow = RISK_WORDS.get(row['fire_risk_tomorrow'], 'Unknown')
        # tooltip_text_tomorrow = f"Land Category: {land_type.capitalize()}<br>Fire Risk: {risk_word_tomorrow}<br>Closest Station: {closest_station}"
        # add_geojson_layer(fire_risk_tomorrow_layer, row['fire_risk_tomorrow'], tooltip_text_tomorrow, geometry, row['fire_risk_tomorrow'])

        # risk_word_five_days = RISK_WORDS.get(row['fire_risk_five_days'], 'Unknown')
        # tooltip_text_five_days = f"Land Category: {land_type.capitalize()}<br>Fire Risk: {risk_word_five_days}<br>Closest Station: {closest_station}"
        # add_geojson_layer(fire_risk_five_days_layer, row['fire_risk_five_days'], tooltip_text_five_days, geometry, row['fire_risk_five_days'])

    legend_html = '''
        <div style="position: fixed; bottom: 50px; left: 50px; width: 140px; height: 180px;
                    border:2px solid grey; z-index:9999; font-size:14px; background-color: white;
                    ">&nbsp;<b>Fire Risk</b><br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:green"></i>&nbsp;Low<br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:blue"></i>&nbsp;Moderate<br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:yellow"></i>&nbsp;High<br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:orange"></i>&nbsp;Very High<br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:red"></i>&nbsp;Extreme
        </div>
    '''
    fire_risk_map.get_root().html.add_child(folium.Element(legend_html))

    fire_risk_today_layer.add_to(fire_risk_map)
    # fire_risk_tomorrow_layer.add_to(fire_risk_map)
    # fire_risk_five_days_layer.add_to(fire_risk_map)

    folium.LayerControl(collapsed=False, position='bottomright').add_to(fire_risk_map)
    Geocoder().add_to(fire_risk_map)

    logging.info("[create_map.py] Saving fire risk map...")
    fire_risk_map.save('./data/output/html/fire_risk_map.html')
    logging.info("[create_map.py] Fire risk map saved successfully.")
