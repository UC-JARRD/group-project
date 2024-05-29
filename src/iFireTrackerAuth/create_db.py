import mysql.connector
import sys
import datetime

# Get today's date
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

config_path = '/home/ubuntu/iFireTrackerAuth/config/'
sys.path.append(config_path)
import config

db_name = config.db_name
db_user = config.db_user
db_user_password = config.db_user_password
db_host = config.db_host

try:
    # Connect to JARRD group MySQL database
    db_connection = mysql.connector.connect(
                host=db_host,
                user=db_user,
                password=db_user_password,
                database=db_name
            )
    print(f'{time} The connection to DB was established.')
    cursor = db_connection.cursor()

    # Create a database jarrd_db
    cursor.execute('CREATE DATABASE IF NOT EXISTS jarrd_db')
    cursor = db_connection.cursor()

    # # DROP tables
    # cursor.execute('''
    #     DROP TABLE users;
    #     DROP TABLE fire_predictions;
    #     DROP TABLE fire_predictions_files;
    # ''')
    # if cursor.rowcount == 0:
    #     print("Tables were deleted successfully")
    # else:
    #     print("No tables were deleted")
        

    # Create a table users
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            login VARCHAR(255) NOT NULL,
            pass VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL
        )
    ''')

    # Create a table fire_predictions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fire_predictions (
            prediction_id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE NOT NULL,
            land_type VARCHAR(255) NOT NULL,
            closest_station_id INT NOT NULL,
            closest_station_name VARCHAR(255) NOT NULL,
            fire_risk_today INT NOT NULL,
            fire_risk_tomorrow INT NOT NULL,
            fire_risk_five_days INT NOT NULL,
            geometry VARCHAR(255) NOT NULL
        )
    ''')

    # Create a table fire_predictions_files
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fire_predictions_files (
            prediction_file_id INT AUTO_INCREMENT PRIMARY KEY,
            date DATE NOT NULL,
            html_file_name VARCHAR(255) NOT NULL,
            csv_file_name VARCHAR(255) NOT NULL
        )
    ''')

    # cursor.execute('''
    #     CREATE TABLE IF NOT EXISTS fire_predictions_files (
    #         prediction_file_id INT AUTO_INCREMENT PRIMARY KEY,
    #         date DATE NOT NULL,
    #         html_file_name VARCHAR(255) NOT NULL,
    #         # html_file LONGBLOB NOT NULL,
    #         csv_file_name VARCHAR(255) NOT NULL,
    #         csv_file LONGBLOB NOT NULL
    #     )
    # ''')

    print(f'{time} The tables were created')
except mysql.connector.Error as err:
    print(f'{time} The tables were created unsuccessful, error was appeared!')

# Close the database connection
cursor.close()
db_connection.close()
