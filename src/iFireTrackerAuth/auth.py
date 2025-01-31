from flask import Flask, jsonify, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import datetime
import sys

# Get today's date
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

config_path = '/home/ubuntu/iFireTrackerAuth/config/'
sys.path.append(config_path)
import config

db_name = config.db_name
db_user = config.db_user
db_user_password = config.db_user_password
db_host = config.db_host
secret_key = config.secret_key

# db_name = os.path.expandvars('$DB_NAME')
# db_user = os.path.expandvars('$DB_USER')
# db_user_password = os.path.expandvars('$DB_PASSWORD')
# db_host = os.path.expandvars('$DB_HOST')

app = Flask(__name__)
app.secret_key = secret_key

# JWT_SECRET = "your_jwt_secret_key"
# JWT_ALGORITHM = "HS256"

@app.route("/")
def hello_world():
    return "Test"

@app.route("/register", methods=["POST"])
def register():
    # Get data from POST request
    name = request.form.get('name')
    login = request.form.get('login')
    email = request.form.get('email')
    password = request.form.get('password')

    if not login or not email or not password:
        return "Missing information", 400

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    # Save to a file
    with open("users.txt", "a") as file:
        file.write(f"{login},{email},{hashed_password}\n")

    try:
        db_connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_user_password,
            database=db_name
        )
        print(f'{time} The connection to DB was established.')

# Create cursor
        cursor = db_connection.cursor()

        # Check if the user already exists
        cursor.execute("SELECT COUNT(*) FROM users WHERE login = %s", (login,))
        user_count = cursor.fetchone()[0]
        if user_count > 0:
            return "User already exists in the database."

        # Insert user data into the database
        sql = "INSERT INTO users (name, login, pass, email) VALUES (%s, %s, %s, %s)"
        val = (name, login, hashed_password, email)
        cursor.execute(sql, val)
        db_connection.commit()

        # Close cursor and database connection
        cursor.close()
        db_connection.close()
        print(f'{time} User registered successfully!')
        return "User registered successfully!"

    except mysql.connector.Error as err:
        print(f'{time} User registered unsuccessful, error was appeared!')
        return f"Error: {err}", 500


@app.route("/login", methods=["POST"])
def login():
    # Get data from POST request
    data = request.get_json()
    login = data.get('login')
    password = data.get('password')

    if not login or not password:
        print(f'{time} Missing login or password')
        return "Missing login or password", 400

    try:
        db_connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_user_password,
            database=db_name
        )

        # Create cursor
        cursor = db_connection.cursor()

        # Query user data from the database
        sql = "SELECT login, pass FROM users WHERE login = %s"
        cursor.execute(sql, (login,))
        user = cursor.fetchone()

        # Close cursor and database connection
        cursor.close()
        db_connection.close()

        # if user and check_password_hash(user[1], password):
        #     # Generate JWT token
        #     token = jwt.encode({
        #         'user': login,
        #         'exp': datetime.now(timezone.utc) + datetime.timedelta(hours=24)
        #     }, JWT_SECRET, algorithm=JWT_ALGORITHM)

        #     return jsonify({'token': token})

        #else:
         #    return "Invalid login or password", 401

        if user and check_password_hash(user[1], password):
             # Set session
             session['user'] = login
             print(f'{time} Login successful!')
             return "Login successful!"
        else:
            print(f'{time} Invalid login or password')
            return "Invalid login or password", 401

    except mysql.connector.Error as err:
            return f"Error: {err}", 500

@app.route("/logout")
def logout():
    session.pop('user', None)
    print(f'{time} Logged out successfully!')
    return "Logged out successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
