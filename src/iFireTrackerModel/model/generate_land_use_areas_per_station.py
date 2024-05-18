from shapely.geometry import MultiPolygon, Polygon
from shapely.ops import unary_union  
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

def generate_land_use_areas_per_station():

    # Load station location data
    weather_stations = pd.read_csv('./data/input/canterbury_weather_stations.csv') # coordinates of each station
    # Convert weather station coordinates to GeoDataFrame
    geometry = [Point(xy) for xy in zip(weather_stations['longitude'], weather_stations['latitude'])]
    weather_stations = gpd.GeoDataFrame(weather_stations, geometry=geometry)

    # Load LUCAS NZ land use map data (shapefile)
    land_use_data = gpd.read_file('./data/input/lucas-nz-land-use-map-1990-2008-2012-2016-v011.shx') # Can reduce row numbers using e.g. rows=1000
    # Set the coordinate system
    land_use_data = land_use_data.to_crs("EPSG:4326")
    # Drop unnecessary columns
    columns_to_keep = ['geometry', 'LUCID_2016', 'LUCNA_2016']
    land_use_data = land_use_data[columns_to_keep]

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
    
    # Find the closest weather station for each polygon
    land_use_data['closest_station'] = land_use_data.geometry.apply(lambda x: weather_stations.geometry.distance(x).idxmin())

    # Group the polygons by closest_station and land_type
    grouped = land_use_data.groupby(['closest_station', 'land_type'])

    # A function to merge geometries in a group into a single representative geometry
    def merge_geometries(group):
        polygons = list(group['geometry'])
        if len(polygons) == 1:
            return polygons[0]
        else:
            return unary_union(polygons)

    # Apply the function to each group and create a new DataFrame with the results
    merged_geometries = grouped.apply(merge_geometries).reset_index(name='merged_geometry')

    # Get the name of the closest station for each polygon
    merged_geometries['closest_station_name'] = land_use_data['closest_station'].apply(lambda x: weather_stations.loc[x, 'station_name'])

    merged_geometries.to_csv('./data/input/merged/land_use_areas_per_station.csv', index=False)
    print('Data saved to "./data/input/merged/land_use_areas_per_station.csv" successfully.')

    return merged_geometries

# Run function
generate_land_use_areas_per_station()