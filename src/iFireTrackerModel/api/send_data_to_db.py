import mysql.connector
import datetime
import csv

# Get today's date
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Connect to JARRD group MySQL database
db_config = {
    'user': 'ucstudent',
    'password': 'DATA472JARRDmads',
    'host': 'data472-rna104-jarrd-db.cyi9p9kw8doa.ap-southeast-2.rds.amazonaws.com',
}

db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()

# Create a new database
db_config['database'] = 'jarrd_db'
db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()

csv_file_name = 'fire_risk_per_polygon.csv'
csv_file_path = f'../model/data/input/{csv_file_name}'
html_file_name = 'fire_risk_map.html'
html_file_path = f'../model/data/output/html/{html_file_name}'

# Get the current date and time
system_date = datetime.datetime.now()

# Format the date as a string in the format YYYY-MM-DD
date = system_date.strftime('%Y-%m-%d')

# Print the date string
print(date)

csv.field_size_limit(10000000)

# Open the CSV file
csv_file = open(csv_file_path, 'r')

# Read the CSV file and insert the data into the MySQL table
reader = csv.reader(csv_file)

# Skip the header row
next(reader)  

print(f'{time} The process of filling out the fire_predictions table is in progress...')

i = 0
for row in reader:
    # Extract only the columns we want to insert
    land_type = row[3]
    closest_station_id = row[4]
    closest_station_name = row[5]
    fire_risk_today = row[6]
    fire_risk_tomorrow = row[7]
    fire_risk_five_days = row[8]
    polygon_wkt = row[0]

    i += 1
    # print(f"row : {i}")
    # Insert the data into the MySQL table
    cursor.execute('''
                   INSERT INTO fire_predictions
                   (date, land_type, closest_station_id, closest_station_name, fire_risk_today, fire_risk_tomorrow, fire_risk_five_days, geometry) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, ST_GeomFromText(%s))''', 
                   (date, land_type, closest_station_id, closest_station_name, fire_risk_today, fire_risk_tomorrow, fire_risk_five_days, polygon_wkt)
                   )

# # Commit the changes and close the connections
db_connection.commit()
print(f'{time} The data was inserted into fire_predictions table')


# Open the file in binary mode and read the data
# with open(csv_file_path, 'rb') as csv_file:
#     csv_file_data = csv_file.read()

# with open(html_file_path, 'rb') as html_file:
#     html_file_data = html_file.read()

print(f'{time} The process of filling out the fire_predictions_files table is in progress...')

# Insert the file into the large_files table
cursor.execute("INSERT INTO fire_predictions_files (date, html_file_name, csv_file_name) VALUES (%s, %s, %s)",
               (date, html_file_name, csv_file_name))

# Commit the changes and close the connections
db_connection.commit()
print(f'{time} The data was inserted into fire_predictions_files table')

# Close the database connection
cursor.close()
db_connection.close()
