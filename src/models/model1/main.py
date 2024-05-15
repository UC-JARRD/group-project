import load_data
import process_data
import create_map

def main():
    
    # Load the data
    station_fire_risk, land_use_data = load_data.load_data()
    print('Data loaded successfully.')

    # Process the data
    fire_risk_per_land_use_area = process_data.process_data(station_fire_risk, land_use_data)
    print('Data processed successfully.')

    # # Save fire_risk_per_polygon DataFrame to CSV
    # fire_risk_per_polygon.to_csv('src/models/model1/data/fire_risk_per_polygon.csv', index=False)
    # print('Data saved to "src/models/model1/data/fire_risk_per_polygon.csv" successfully.')

    # Create the map
    create_map.create_map(fire_risk_per_land_use_area)
    print('Map created successfully.')

if __name__ == "__main__":
    main()