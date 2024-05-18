
import os
import boto3
import pandas as pd

# Retrieve data from S3
s3 = boto3.client('s3')

bucket_name = 'data472-rna104-jarrd-hdd'

# Getting CSV data from S3

csv_filename = 'ifiretracker_data/csv/fire_risk_per_land_use_area.csv'
csv_response = s3.get_object(Bucket=bucket_name, Key=csv_filename)
csv_data = pd.read_csv(csv_response['Body'])

# Define the path to the local CSV file
csv_path = './data/csv/fire_risk_per_land_use_area.csv'

# Create the directory path for the CSV file if it doesn't exist
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# Save the DataFrame to the local CSV file
csv_data.to_csv(csv_path, index=False)


# Getting HTML map from S3

html_filename = 'ifiretracker_data/html/fire_risk_map.html'
html_response = s3.get_object(Bucket=bucket_name, Key=html_filename)

# Define the path to the local HTML file
html_path = './data/html/fire_risk_map.html'

# Create the directory path for the HTML file if it doesn't exist
os.makedirs(os.path.dirname(html_path), exist_ok=True)

# Save the HTML file to the local filesystem
with open(html_path, 'wb') as html_file:
    html_file.write(html_response['Body'].read())

