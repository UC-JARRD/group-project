import mysql.connector

# Connect to Roman individual MySQL database
# db_config = {
#     'user': 'admin',
#     'password': 'yeaWYdvmiGhJpjmFh0d4',
#     'host': 'data472-rna104-db.cyi9p9kw8doa.ap-southeast-2.rds.amazonaws.com',
# }

# Connect to JARRD group MySQL database
db_config = {
    'user': 'ucstudent',
    'password': 'DATA472JARRDmads',
    'host': 'data472-rna104-jarrd-db.cyi9p9kw8doa.ap-southeast-2.rds.amazonaws.com',
}

db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()

# Create a database jarrd_db
cursor.execute('CREATE DATABASE IF NOT EXISTS jarrd_db')
db_config['database'] = 'jarrd_db'
db_connection = mysql.connector.connect(**db_config)
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

print('The tables were created')

# Close the database connection
cursor.close()
db_connection.close()