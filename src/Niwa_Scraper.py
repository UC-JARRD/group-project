from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time
from io import StringIO
from bs4 import BeautifulSoup

"""This code looks through the niwa website to find their fire risks
for today, tomorrow and 5 days from now. These are saved as Firedata.csv."""

# URL of the NIWA Canterbury fire weather page
URL = 'https://fireweather.niwa.co.nz/region/Canterbury'

# Set up Firefox options
options = Options()
options.add_argument('--headless')  # Run in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Define driver as Firefox webdriver
driver = webdriver.Firefox(options=options)

# Load the page in Firefox
driver.get(URL)

# Allow some time for the page and JavaScript to fully load
time.sleep(5)

# Function to scrape data for the current slider position
def scrape_table():
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
        
        return df

    except Exception as e:
        print(f"An error occurred while scraping: {str(e)}")
        return None

# List of columns to drop
columns_to_drop = ['FFMC', 'DMC', 'DC', 'ISI', 'BUI', 'FWI', 'TEMP', 'RH', 'DIR', 'WSP', 'RN24', 'GC%']

# Create an empty DataFrame to store the combined data
combined_df = pd.DataFrame()

# Scrape data for today, tomorrow, and five_days
for offset, suffix in zip([-172 * 2, -172, 172 *3], ['today', 'tomorrow', 'five_days']):
    # Interact with the slider to set it to the desired day
    slider = driver.find_element(By.ID, 'niwa_slider')
    action = ActionChains(driver)
    
    #This needs to be adjusted to move the slider as desired.
    action.click_and_hold(slider).move_by_offset(offset, 0).release().perform()  # Adjust offset as necessary
    time.sleep(2)  # Wait for the page to update

    # Scrape the table for the current slider position
    df = scrape_table()
    if df is not None:
        #removing any uneeded columns
        for column in columns_to_drop:
            if column in df.columns:
                df.drop(columns=[column], inplace=True)
        
        #making varible names line up with the fire models requirements.
        df.rename(columns={'STATION NAME': 'station_name'}, inplace=True)
        df[f'{suffix}_forest'] = df['FOREST']
        df[f'{suffix}_scrub'] = df['SCRUB']
        df[f'{suffix}_grass'] = df['GRASS']
        df.drop(columns=['FOREST', 'SCRUB', 'GRASS'], inplace=True)
        
        # Merge with the combined DataFrame
        if combined_df.empty:
            combined_df = df
        else:
            combined_df = pd.merge(combined_df, df, on='station_name')

# Save to a CSV
combined_df.to_csv('Firedata.csv', index=False)

# Display the combined DataFrame
print(combined_df)

# Close the browser
driver.close()
