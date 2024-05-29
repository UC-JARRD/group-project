import requests
import datetime
import sys
import os
config_path = f'{os.path.expandvars('$MODEL_SERVER_PATH')}/config/'
sys.path.append(config_path)
import config

# Get today's date
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Set the API endpoint URL
url = f'{config.web_server_url}/upload?format=csv'

# Set the path to the CSV file you want to send
csv_path = config.csv_output_local_path

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