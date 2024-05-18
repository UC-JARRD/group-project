from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import sys
import time
from io import StringIO
from bs4 import BeautifulSoup

#This returns a table from Niwa.
#It takes a few seconds to run as has to wait for the table to load.
#It returns a dataframe.

# URL of the NIWA Canterbury fire weather page
URL = 'https://fireweather.niwa.co.nz/region/Canterbury'

# Define driver as Firefox webdriver
driver = webdriver.Firefox()
    
# Load the page in Firefox
driver.get(URL)

# Allow some time for the page and JavaScript to fully load
time.sleep(5)

# Get the html element containing the table
try:
    element = driver.find_element(By.ID, 'mainTable')
    element_html = element.get_attribute('innerHTML')

    # Convert the HTML string to a StringIO object
    html_buffer = StringIO(element_html)
    
    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_buffer, 'html.parser')

    # Find the table headers
    headers = [header.text.strip() for header in soup.find_all('th')]

    # Find the table rows
    rows = []
    for row in soup.find_all('tr'):
        cells = row.find_all(['td', 'th'])
        cells = [cell.get_text(strip=True) for cell in cells]
        if cells:  # Only add non-empty rows
            rows.append(cells)

    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=headers)
    
    # Deleting the first row as values are repeated
    df = df.drop(df.index[0])

    # Display the DataFrame
    print(df)

except Exception as e:
    print(f"An error occurred: {str(e)}")
finally:
    # Close the browser
    driver.close()
    
    # Now you can close the StringIO object after use
    html_buffer.close()
