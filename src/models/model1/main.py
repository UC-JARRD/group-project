import load_data
import process_data
import create_map

def main():
    # Load the data
    weather_data, land_use_data = load_data.load_data()
    print('Data loaded successfully.')

    # Process the data
    land_use_data = process_data.process_data(weather_data, land_use_data)
    print('Data processed successfully.')

    # Create the map
    create_map.create_map(land_use_data)
    print('Map created successfully.')

if __name__ == "__main__":
    main()