import yaml

web_server_path = '/home/ubuntu/iFireTrackerWeb'
CONFIG = f'{web_server_path}/config/config.yaml'

with open(CONFIG, 'r') as file:
    data = yaml.safe_load(file)

# urls
s3_bucket_name = data['url']['s3_bucket_name']
auth_server_url = data['url']['auth_server_url']

# s3 filenames
csv_s3_filename = data['path']['csv_s3_filename']
html_s3_filename = data['path']['html_s3_filename']

# web server local filenames
csv_local_path = f'{web_server_path}/{data['path']['csv_local_path']}'
html_local_path = f'{web_server_path}/{data['path']['html_local_path']}'

# maximum allowed size for HTTP requests
max_content_length = data['system']['max_content_length']

