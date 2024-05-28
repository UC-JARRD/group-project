from flask import Flask, request, render_template, render_template_string, redirect, url_for
import pandas as pd
import requests
import sys

config_path = '/home/ubuntu/iFireTrackerWeb/config/'
sys.path.append(config_path)
import config

app = Flask(__name__)

AUTH_SERVER_URL = config.auth_server_url

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']  # Assuming you're collecting 'name' in the form.
        login = request.form['username']
        email = request.form['email']  # Assuming you're collecting 'email' in the form.
        password = request.form['password']

        # Form the API request to the authorization server
        response = requests.post(f'{AUTH_SERVER_URL}/register', data={'name': name,'login': login,'email': email,'password': password})

        if response.status_code == 200 or response.status_code == 201:
            return redirect(url_for('login'))
        else:
            return 'Registration failed', response.status_code

    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        # Form the API request to the authorization server
        response = requests.post(f'{AUTH_SERVER_URL}/login', json={'login': login, 'password': password})

        if response.status_code == 200 or response.status_code == 201:
            return redirect(url_for('main'))
        else:
            return 'Login failed', response.status_code

    return render_template('login.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/map', methods=['GET'])
def map():
    print('Get the Map page...')
    
    html_path = config.html_local_path
    
    # Read the contents of the HTML file
    with open(html_path, 'r') as html_file:
        html_contents = html_file.read()

    # Render an HTML template with the HTML contents
    return render_template_string(html_contents)

@app.route('/csv', methods=['GET'])
def csv():
    print('Get the CSV page...')
    
    csv_path = config.csv_local_path
    
    # Read the CSV file
    df_origin = pd.read_csv(csv_path)
    
    # Drop the "school" column from the DataFrame
    df = df_origin.drop(columns=['merged_geometry'])
    
    # Get the headers (column names)
    headers = df.columns.tolist()

    # Get the rows (data) as a list of lists
    rows = df.values.tolist()

    print('Display CSV file as HTML page.')
    # Render an HTML template with the header and rows
    # return render_template_string(html_template)
    return render_template('csv.html', header=headers, rows=rows)

# Set the maximum allowed size for HTTP requests to 10 MB
app.config['MAX_CONTENT_LENGTH'] = int(config.max_content_length)

# Set the upload endpoint URL
@app.route('/upload', methods=['POST'])
def upload_file():
    # Get the request data
    format = request.args.get('format')
    data = request.data

    if format == 'csv':
        # Set the path to save the CSV file
        save_csv_path = config.csv_local_path

        # Save the CSV file to the filesystem
        with open(save_csv_path, 'wb') as csv_file:
            csv_file.write(data)

        # Return a success response
        return 'CSV file uploaded successfully', 200
    elif format == 'html':
        # Set the path to save the HTML file
        save_html_path = config.html_local_path

        # Save the HTML file to the filesystem
        with open(save_html_path, 'wb') as html_file:
            html_file.write(data)

        # Return a success response
        return 'HTML file uploaded successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
