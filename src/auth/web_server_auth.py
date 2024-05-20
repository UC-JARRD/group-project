from flask import Flask, request, jsonify, render_template, redirect, url_for
import requests

app = Flask(__name__)

AUTH_SERVER_URL = 'http://13.239.55.4:5000'

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form['name']  # Assuming you're collecting 'name' in the form.
        login = request.form['username']
        email = request.form['email']  # Assuming you're collecting 'email' in the form.
        password = request.form['password']

        # Form the API request to the authorization server
        response = requests.post(f'{AUTH_SERVER_URL}/register', data={'name': name,'login': login,'email': email,'password': password})

        if response.status_code == 201:
            return redirect(url_for('login'))
        else:
            return 'Registration failed', response.status_code

    return render_template('registration.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form['username']
        password = request.form['password']

        # Form the API request to the authorization server
        response = requests.post(f'{AUTH_SERVER_URL}/login', json={'username': login, 'password': password})

        if response.status_code == 200:
            return redirect(url_for('dashboard'))
        else:
            return 'Login failed', response.status_code

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)