
import boto3
import pandas as pd
import datetime
import sys
import os
config_path = f'{os.path.expandvars('$MODEL_SERVER_PATH')}/config/'
print(config_path)
sys.path.append(config_path)
import config

# Get today's date
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Retrieve data from S3
s3 = boto3.client('s3')

bucket_name = config.s3_bucket_name

# Define the path to CSV/HTML files on S3
csv_filename = config.csv_s3_filename
html_filename = config.html_s3_filename

# Define the path to the local CSV/HTML files
csv_path = config.csv_output_local_path
html_path = config.html_output_local_path


# Upload the CSV file to the S3 bucket
s3.put_object(
    Bucket=bucket_name,
    Key=csv_filename,
    Body=open(csv_path, 'rb')
)
print(f'{time} The CSV data was sent to S3 bucket successfully')


# Upload the HTML file to the S3 bucket
s3.put_object(
    Bucket=bucket_name,
    Key=html_filename,
    Body=open(html_path, 'rb')
)
print(f'{time} The HTML data was sent to S3 bucket successfully')
