#!/bin/bash
cd /home/ubuntu/iFireTrackerWeb
source venv/bin/activate

# Get prediction files from S3
python3 get_files_from_s3.py >> ./logs/get_s3.log 2>> ./logs/get_s3_error.log