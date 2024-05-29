# Niwa Scraper

This scrapes the https://fireweather.niwa.co.nz/region/Canterbury website to get fire risks for different terrain over the Canterbruy region. It selects for today, tomorrow and 5 days time.

## Description

The scraper looks for the mainTable and niwa_slider elements. It adjusts the slider values for differnt predictions. It then waits for Niwas server to load the table. Once extracted, uneeded columns are dropped and the data is cleaned. The data is saved as a CSV for use in predicting fire.

The scraper can be easily scaled up to the entire country by scraping each region set by Niwa. Note the terrain types are not scraped from Niwa.

### Dependencies

    pip install selenium pandas BeautifulSoup


This runs using Firefox with geckodriver
https://github.com/mozilla/geckodriver/releases

Note chrome struggled to scrape Niwa's website.

## Installation in a AWS EC2 instance
1. **Create an EC2 instance**
    We used a ubuntu instance.

2. **Clone the repository**:
    ```bash
    git clone https://github.com/UC-JARRD/iFireTracker/tree/main.git
    cd src/scraper
    ```

3. **Create a virtual environment**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate
    ```
4. **Install the above dependances.**

5. **Run a cron job each day**:

    This makes the file run each day. The first set of numbers defines when the script runs. The first path is to python. The second is to the scraper. Ensure this saves the CSV in the correct directory for the model to run it.

    An example path, running daily at midnight:
    ```bash
    0 0 * * * /home/ubuntu/myenv/bin/python /home/ubuntu/Niwa Scraper.py 
    ```

## Debugging

The scaper can be act differently depending on the system running them. It will change behavour depending on window size. Adjust the window size and slider mouse clicks to handle this.

    driver.set_window_size(1920, 1080) 
    zip([-172 * 2, -172, 172 *3]). 
    
Commenting out headless mode will help with debugging.
    options.add_argument('--headless')  