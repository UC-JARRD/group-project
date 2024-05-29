import yaml

auth_server_path = '/home/ubuntu/iFireTrackerAuth'
CONFIG = f'{auth_server_path}/config/config.yaml'

with open(CONFIG, 'r') as file:
    data = yaml.safe_load(file)

# urls
db_name = data['db_name']
db_user = data['db_user']
db_user_password = data['db_user_password']
db_host = data['db_host']
secret_key = data['secret_key']

