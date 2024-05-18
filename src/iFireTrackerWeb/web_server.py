import io
from flask import Flask, request, Response, render_template, render_template_string, send_file
import pandas as pd

app = Flask(__name__)

def message():
    error_message = "Unknown format of data!"

    # Create an HTML template with the message
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Message</title>
    </head>
    <body>
        <h1>{error_message}</h1>
    </body>
    </html>
    """

    return render_template_string(html_template)

# Set the get endpoint URL
@app.route('/query', methods=['GET'])
def query():
    print('Get the Main page...')
    format = request.args.get('format')
    
    csv_path = './data/csv/fire_risk_per_land_use_area.csv'
    html_path = './data/html/fire_risk_map.html'
    
    if format == 'csv':
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
    elif format == 'html':
        # Read the contents of the HTML file
        with open(html_path, 'r') as html_file:
            html_contents = html_file.read()

        # Render an HTML template with the HTML contents
        # return render_template('html.html', html_contents=html_contents)
        return render_template_string(html_contents)
    else:
        print('Unknown format of data!')
        return message()
    
# Set the upload endpoint URL
@app.route('/upload', methods=['POST'])
def upload_file():
    # Get the request data
    format = request.args.get('format')
    data = request.data

    if format == 'csv':
        # Set the path to save the CSV file
        save_csv_path = './data/csv/fire_risk_per_land_use_area.csv'

        # Save the CSV file to the filesystem
        with open(save_csv_path, 'wb') as csv_file:
            csv_file.write(data)

        # Return a success response
        return 'CSV file uploaded successfully', 200
    elif format == 'html':
        # Set the path to save the HTML file
        save_html_path = './data/html/fire_risk_map.html'

        # Save the HTML file to the filesystem
        with open(save_html_path, 'wb') as html_file:
            html_file.write(data)

        # Return a success response
        return 'HTML file uploaded successfully', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
