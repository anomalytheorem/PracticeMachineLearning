import requests
import csv

# Define the API endpoint and the parameters for the API request
endpoint = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data'
params = {
    'datasetid': 'GHCND',  # Global Historical Climatology Network Daily
    'stationid': 'GHCND:USW00094728',  # Boston, MA
    'startdate': '2010-01-01',
    'enddate': '2010-12-31',
    'limit': 1000,
    'offset': 0
}

# Make the request to the NOAA API
response = requests.get(endpoint, params=params)

# Check the status code of the response
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Open a file for writing the data to a CSV
    with open('weather_data.csv', 'w') as csvfile:
        # Create a CSV writer
        writer = csv.DictWriter


