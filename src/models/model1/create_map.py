import folium

def create_map(land_use_data):
    # Calculate the bounds of the land use data
    bounds = land_use_data.total_bounds

    # Calculate the center of the bounds
    center_lat = (bounds[1] + bounds[3]) / 2
    center_lon = (bounds[0] + bounds[2]) / 2

    # Create a base map centered on New Zealand
    map = folium.Map(location=[center_lat, center_lon], zoom_start=12)

    # Define colors for each fire risk level
    risk_colors = {1: 'green', 2: 'blue', 3: 'yellow', 4: 'orange', 5: 'red'}

    # Define a dictionary to map fire risk numbers to words
    risk_words = {1: 'Low', 2: 'Moderate', 3: 'High', 4: 'Very High', 5: 'Extreme'}

    # Plot polygons on the map, colored by fire risk
    for _, row in land_use_data.iterrows():
        if 'fire_risk' in row:  # Check if 'fire_risk' exists for the current row
            risk_word = risk_words.get(row['fire_risk'], 'Unknown')
            tooltip_text = f"Land Category: {row['land_type']}<br>Fire Risk: {risk_word}<br>Closest Station: {row['closest_station_name']}"
            folium.GeoJson(
                row.geometry,
                style_function=lambda x, risk=row['fire_risk']: {
                    'fillColor': risk_colors.get(risk, 'gray'),
                    'color': 'black',
                    'weight': 1,
                    'fillOpacity': 0.7
                },
                tooltip=folium.Tooltip(tooltip_text, sticky=True)
            ).add_to(map)

    # Add a legend to the map
    legend_html = '''
        <div style="position: fixed; bottom: 50px; left: 50px; width: 140px; height: 180px;
                    border:2px solid grey; z-index:9999; font-size:14px;
                    ">&nbsp;<b>Fire Risk</b><br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:green"></i>&nbsp;Low<br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:blue"></i>&nbsp;Moderate<br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:yellow"></i>&nbsp;High<br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:orange"></i>&nbsp;Very High<br>
                    &nbsp;<i class="fa fa-square fa-2x" style="color:red"></i>&nbsp;Extreme
        </div>
    '''
    map.get_root().html.add_child(folium.Element(legend_html))

    # Save the map as an HTML file
    map.save('src/models/model1/data/maps/fire_risk_map.html')