
import boto3
import pandas as pd
import datetime
import os
import sys
config_path = f'{os.path.expandvars('$WEB_SERVER_PATH')}/config/'
print(config_path)
sys.path.append(config_path)
import config

# Get today's date
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Retrieve data from S3
s3 = boto3.client('s3')

# Define the S3 bucket name
bucket_name = config.s3_bucket_name

# Define the paths to the S3 CSV and HTML files
csv_s3_filename = config.csv_s3_filename
html_s3_filename = config.html_s3_filename

# Define the paths to the local CSV and HTML files
csv_local_path = config.csv_local_path
html_local_path = config.html_local_path

# Getting CSV data from S3
csv_response = s3.get_object(Bucket=bucket_name, Key=csv_s3_filename)
csv_data = pd.read_csv(csv_response['Body'])
print(f'{time} The CSV predictions file was successfully received from S3.')

# Create the directory path for the CSV file if it doesn't exist
os.makedirs(os.path.dirname(csv_local_path), exist_ok=True)

# Save the DataFrame to the local CSV file
csv_data.to_csv(csv_local_path, index=False)
print(f'{time} The CSV predictions file was saved into local filesystem successfully')


# Getting HTML map from S3
html_response = s3.get_object(Bucket=bucket_name, Key=html_s3_filename)
print(f'{time} The HTML predictions file was successfully received from S3.')

# Create the directory path for the HTML file if it doesn't exist
os.makedirs(os.path.dirname(html_local_path), exist_ok=True)

# Save the HTML file to the local filesystem
with open(html_local_path, 'wb') as html_file:
    html_file.write(html_response['Body'].read())
print(f'{time} The HTML predictions file was saved into local filesystem successfully')

