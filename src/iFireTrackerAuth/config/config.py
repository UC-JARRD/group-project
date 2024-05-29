import yaml
import os

s3_bucket_name = os.path.expandvars('$S3_BUCKET_NAME')
web_server_url = os.path.expandvars('$WEB_SERVER_URL')
db_name = os.path.expandvars('$DB_NAME')
db_user = os.path.expandvars('$DB_USER')
db_user_password = os.path.expandvars('$DB_PASSWORD')
db_host = os.path.expandvars('$DB_HOST')
model_server_path = os.path.expandvars('$MODEL_SERVER_PATH')

CONFIG = f'{model_server_path}/config/config.yaml'

with open(CONFIG, 'r') as file:
    data = yaml.safe_load(file)

# s3 filenames
csv_s3_filename = data['csv_s3_filename']
html_s3_filename = data['html_s3_filename']

# model server local filenames
csv_output_local_path = f'{model_server_path}/{data['csv_output_local_path']}'
html_output_local_path = f'{model_server_path}/{data['html_output_local_path']}'
csv_input_fire_risk = f'{model_server_path}/{data['csv_input_fire_risk']}'
csv_input_weather_stations = f'{model_server_path}/{data['csv_input_weather_stations']}'
csv_input_merged_land_stations = f'{model_server_path}/{data['csv_input_merged_land_stations']}'
input_fire_risk_prefix = f'{model_server_path}/{data['input_fire_risk_prefix']}'
shx_input_land_use = f'{model_server_path}/{data['shx_input_land_use']}'

# path to logs
log_path = f'{model_server_path}/{data['log']}'

