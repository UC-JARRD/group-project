import requests

# Set the API endpoint URL
url = 'http://13.211.167.106/upload?format=html'

# Set the path to the CSV file you want to send
html_path = '../model/output/html/fire_risk_map.html'

# Open the CSV file in binary mode
with open(html_path, 'rb') as html_file:
    
    # Set the request headers
    headers = {'Content-Type': 'text/html'}

    # Send the HTTP POST request with the HTML file as the request body
    response = requests.post(url, headers=headers, files={'file': html_file})

    # Check the response status code
    if response.status_code == 200:
        print('HTML file uploaded successfully')
    else:
        print(f'HTML file upload failed with status code {response.status_code}')