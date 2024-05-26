import requests
import datetime

# Get today's date
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Set the API endpoint URL
url = 'http://54.66.144.170/upload?format=csv'

# Set the path to the CSV file you want to send
csv_path = '../../model/data/output/csv/fire_risk_per_land_use_area.csv'

# Open the CSV file in binary mode
with open(csv_path, 'rb') as csv_file:
    # Set the request headers
    headers = {'Content-Type': 'application/octet-stream'}

    # Send the HTTP POST request with the CSV file as the request body
    response = requests.post(url, headers=headers, data=csv_file)

    # Check the response status code
    if response.status_code == 200:
        print(f'{time} CSV file uploaded successfully')
    else:
        print(f'{time} CSV file upload failed with status code {response.status_code}')