import folium
from folium.plugins import Geocoder
from datetime import datetime, timedelta
from shapely.wkt import loads

# Constants
CENTRE_LAT = -43.525650 # Latitude of Christchurch city
CENTRE_LON = 172.639847 # Longitude of Christchurch city
RISK_COLORS = {0: 'transparent', 1: 'green', 2: 'blue', 3: 'yellow', 4: 'orange', 5: 'red'} # To match http://fireweather.niwa.co.nz/region/Canterbury colours
RISK_WORDS = {0: 'Water - No Risk', 1: 'Low', 2: 'Moderate', 3: 'High', 4: 'Very High', 5: 'Extreme'}

def create_map(fire_risk_per_land_use_area):

    # Create a base map centered on New Zealand
    map = folium.Map(location=[CENTRE_LAT, CENTRE_LON], zoom_start=12)

    # Get today's date and calculate the dates for tomorrow and five days from now
    today_date = datetime.now().date()
    tomorrow_date = today_date + timedelta(days=1)
    five_days_date = today_date + timedelta(days=5)

    # Create a LayerGroup for all layers
    all_layers = folium.FeatureGroup()

    # Create layer groups for each fire risk day
    fire_risk_today_layer = folium.FeatureGroup(name=f'Fire Risk for {today_date}', overlay=True, control=True, show=True)
    fire_risk_tomorrow_layer = folium.FeatureGroup(name=f'Fire Risk for {tomorrow_date}', overlay=True, control=True, show=False)
    fire_risk_five_days_layer = folium.FeatureGroup(name=f'Fire Risk for {five_days_date}', overlay=True, control=True, show=False)
    
    # Convert geometry to correct format
    fire_risk_per_land_use_area['geometry'] = fire_risk_per_land_use_area['merged_geometry'].apply(loads)

    # Plot polygons on the map, colored by fire risk
    for _, row in fire_risk_per_land_use_area.iterrows():
        
         # Extract necessary information
        closest_station = row['closest_station_name']
        land_type = row['land_type']
        geometry = row['geometry']

        # Today's fire risk
        risk_word_today = RISK_WORDS.get(row['fire_risk_today'], 'Unknown')
        tooltip_text_today = f"Land Category: {land_type.capitalize()}<br>Fire Risk: {risk_word_today}<br>Closest Station: {closest_station}"
        folium.GeoJson(
            geometry,
            style_function=lambda x, risk=row['fire_risk_today']: {
                'fillColor': RISK_COLORS.get(risk, 'gray'),
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.7
            },
            tooltip=folium.Tooltip(tooltip_text_today, sticky=True)
        ).add_to(fire_risk_today_layer)

        # Tomorrow's fire risk
        risk_word_tomorrow = RISK_WORDS.get(row['fire_risk_tomorrow'], 'Unknown')
        tooltip_text_tomorrow = f"Land Category: {land_type.capitalize()}<br>Fire Risk: {risk_word_tomorrow}<br>Closest Station: {closest_station}"
        folium.GeoJson(
            geometry,
            style_function=lambda x, risk=row['fire_risk_tomorrow']: {
                'fillColor': RISK_COLORS.get(risk, 'gray'),
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.7
            },
            tooltip=folium.Tooltip(tooltip_text_tomorrow, sticky=True)
        ).add_to(fire_risk_tomorrow_layer)

        # Five days' fire risk
        risk_word_five_days = RISK_WORDS.get(row['fire_risk_five_days'], 'Unknown')
        tooltip_text_five_days = f"Land Category: {land_type.capitalize()}<br>Fire Risk: {risk_word_five_days}<br>Closest Station: {closest_station}"
        folium.GeoJson(
            geometry,
            style_function=lambda x, risk=row['fire_risk_five_days']: {
                'fillColor': RISK_COLORS.get(risk, 'gray'),
                'color': 'black',
                'weight': 1,
                'fillOpacity': 0.7
            },
            tooltip=folium.Tooltip(tooltip_text_five_days, sticky=True)
        ).add_to(fire_risk_five_days_layer)
    
    # Add a legend to the map
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
    map.get_root().html.add_child(folium.Element(legend_html))

    # Add the layer groups to the main layer group
    fire_risk_today_layer.add_to(map)
    fire_risk_tomorrow_layer.add_to(map)
    fire_risk_five_days_layer.add_to(map)

    # Add a layer control to the map
    folium.LayerControl(collapsed=False, position='bottomright').add_to(map)

    # Add a search bar to the map
    Geocoder().add_to(map)

    # Save the map as an HTML file
    map.save('src/models/model1/data/maps/fire_risk_map.html')
  