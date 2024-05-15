# aws s3 cp metadata_v1.1.0.csv s3://data472-jkn35-metadata-fungi-observations/metadata

import boto3
import pandas as pd

 # Retrieve metadata from S3 based on the specified version
s3 = boto3.client('s3')
bucket_name = 'data472-rna104-hdd'
# prefix = 'metadata/metadata_v'  # Metadata is stored with names like "metadata_v1-0-0.csv"


# if metadata_version == 'LATEST':
#     # List objects in the metadata folder
#     response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    
#     # Extract version numbers from object keys
#     versions = [re.findall(r'metadata_v(\d+-\d+-\d+)', obj['Key'])[0] for obj in response.get('Contents', [])]
    
#     # Find the latest version
#     latest_version = max(versions)
    
#     # Construct key for the latest metadata file
#     key = f'{prefix}{latest_version}.csv'

# else:
#     key = f'{prefix}{metadata_version}.csv'  # Assuming metadata is stored in CSV format

try:
    response = s3.get_object(Bucket=bucket_name, Key=key)
    metadata_df = pd.read_csv(response['Body'])

except Exception as e:
    return {
        "statusCode": 500,
        "body": json.dumps({"error": str(e)})
    }