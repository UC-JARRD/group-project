# Niwa Scraper

This scrapes the https://fireweather.niwa.co.nz/region/Canterbury website to get fire risks for different terrain over the Canterbruy region. It selects for today, tomorrow and 5 days time.

## Description

The scraper looks for the mainTable and niwa_slider elements. It adjusts the slider values for differnt predictions. It then waits for Niwas server to load the table. Once extracted, uneeded columns are dropped and the data is cleaned. The data is saved as a CSV for use in predicting fire.

The scraper can be easily scaled up to the entire country by scraping each region set by Niwa. Note the terrain types are not scraped from Niwa. 

### Dependencies

    ```bash
    pip install selenium pandas BeautifulSoup
    ```

    This runs using Firefox with geckodriver
    https://github.com/mozilla/geckodriver/releases

    Note chrome struggled to scrape Niwa's website.

## Installation in a AWS EC2 instance

1. **Clone the repository**:
    ```bash
    git clone https://github.com/UC-JARRD/iFireTracker/tree/main.git
    cd src/scraper
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate
    ```
3. **Install the above dependances.**

4. **Run a cron job each day**:

    The first set of numbers defines when the script runs.
    The first path is to python. The second is to the scraper.

    An example path, running daily at midnight:
    ```bash
    0 0 * * * /home/ubuntu/myenv/bin/python /home/ubuntu/Niwa Scraper.py 
    ```
