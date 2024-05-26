
import boto3
import pandas as pd
import datetime

# Get today's date
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Retrieve data from S3
s3 = boto3.client('s3')

bucket_name = 'data472-rna104-jarrd-hdd'
csv_filename = 'ifiretracker_data/csv/fire_risk_per_land_use_area.csv'
# Define the path to the local CSV file
csv_path = '../model/data/output/csv/fire_risk_per_land_use_area.csv'

# Upload the CSV file to the S3 bucket
s3.put_object(
    Bucket=bucket_name,
    Key=csv_filename,
    Body=open(csv_path, 'rb')
)
print(f'{time} The CSV data was sent to S3 bucket successfully')


html_filename = 'ifiretracker_data/html/fire_risk_map.html'
# Define the path to the local HTML file
html_path = '../model/data/output/html/fire_risk_map.html'

# Upload the HTML file to the S3 bucket
s3.put_object(
    Bucket=bucket_name,
    Key=html_filename,
    Body=open(html_path, 'rb')
)
print(f'{time} The HTML data was sent to S3 bucket successfully')
