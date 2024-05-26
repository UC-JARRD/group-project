#!/bin/bash
cd /home/ubuntu/iFireTrackerModel
source venv/bin/activate

# Set the yesterday date and time
yesterday=$(date -d 'yesterday' +"%Y-%m-%d")

# Set the source and destination file paths
src_file="./model/data/input/everyday_data/${yesterday}_fire_risk.csv"
dst_file="./model/data/input/everyday_data/$(date +"%Y-%m-%d")_fire_risk.csv"

# Copy the file - this is a temporary solution until Scrapper works automatically. 
# For a permanent data delivery solution, you need to comment out these lines
cp "$src_file" "$dst_file"

# Run the model
cd model
python3 main.py >> ../logs/run_model.log 2>> ../logs/run_model_error.log

# Send files to Web Server, DB, and S3
cd ../api
python3 send_data_to_db.py >> ../logs/send.log 2>> ../logs/send_error.log
python3 send_files_to_s3.py >> ../logs/send.log 2>> ../logs/send_error.log
cd api-to-webserver
python3 send_csv_to_webserver.py >> ../../logs/send.log 2>> ../../logs/send_error.log
python3 send_html_to_webserver.py >> ../../logs/send.log 2>> ../../logs/send_error.log