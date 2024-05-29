# Modelling Fire Risk - Research

## This website shows the fire risk in large areas of NZ
https://fireweather.niwa.co.nz/indices - requires webscraping, but seemingly has all data required

## Models

### AI geospatial wildfire risk prediction (USA) 
https://towardsdatascience.com/ai-geospatial-wildfire-risk-prediction-8c6b1d415eb4

### New Zealand Fire Risk Assessment
https://environment.govt.nz/publications/fire-risk-assessment-a-measure-to-quantify-fire-risk-for-new-zealand-locations/



## Datasets / Data Sources

### Previous forest fires in Christchurch
2017 
https://ccc.govt.nz/environment/land/fire/porthillsfire/

2024
https://en.wikipedia.org/wiki/2024_Port_Hills_fire


### Land use maps of NZ
https://data.mfe.govt.nz/data/


### LiDAR elevation data
https://canterburymaps.govt.nz/help/imagery-and-elevation-data-lidar/elevation-data-lidar/

### Fire Incident Reports 
Reports are daily, and up to 7 days previous are available, but they do not have much useful detail.
https://www.fireandemergency.nz/incidents-and-news/incident-reports/incidents?region=3&day=Friday


###  Open Meteo
#### Weather forecast
Free weather data!
Daily and hourly data available. 
Provides forecasts for up to 16 days.
This dataset has past data only from up to 3 months prior.
https://open-meteo.com/en/docs/ 

#### Historical weather
The historical weather has data from 1940 - today.
However, there is a **5-day delay** in the data.
This could be used to train a model if we need to.
https://open-meteo.com/en/docs/historical-weather-api/

#### Climate change prediction
Climate change predictions until 2050.
May not be relevant depending on what we plan to do.
https://open-meteo.com/en/docs/climate-api/


### Metservice
$ Weather data but it costs to use API. 
Free plan goes up to '100 API units'.
https://www.metservice.com/point-forecast-api/faq/



