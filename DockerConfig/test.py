import requests
import pandas as pd

# API base URL
url = 'https://health.gov/myhealthfinder/api/v3/topicsearch.json'

# Request parameters (if necessary)
params = {
    'lang': 'en'
}

# Make the GET request
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Get the data from the response in JSON format
    data = response.json()
    
    resources = data['Result']['Resources']['Resource']

    # Convert 'Resources' to a pandas DataFrame
    df = pd.DataFrame(resources)
    
    # Display the DataFrame
    print('This is df2, let''s compare!:\n',df)
else:
    print('Error in the request:', response.status_code)