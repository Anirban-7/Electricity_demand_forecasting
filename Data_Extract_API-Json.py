import requests
import json


# Enter API url
api_url = "https://api.eia.gov/v2/electricity/rto/region-data/data/?frequency=hourly&data[0]=value&start=2018-07-01T00&end=2018-07-10T00&sort[0][column]=period&sort[0][direction]=desc&offset=0&length=5000"
api_key = "Enter actual API key for eia website here"  

# Parameters
params = {
    "api_key": api_key,
    "frequency": "hourly",
    "data[0]": "value",
    "start": "2018-07-01T00",
    "end": "2018-07-10T00",
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "offset": 0,
    "length": 5000
}

try:
    all_data = []

    while True:
        response = requests.get(api_url, params=params)

        if response.status_code == 200:
            data = response.json()
            
            if 'response' in data and 'data' in data['response']:
                current_data = data['response']['data']
                all_data.extend(current_data)
                print(f"Retrieved {len(current_data)} records. Total: {len(all_data)}")
                
                # Check if the retrieved data is less than 5000 records
                if len(current_data) < 5000:
                    break
            else:
                break

            # Offset for the next request
            params['offset'] += 5000
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")
            break

    # Save data
    with open("data.json", "w") as file:
        json.dump(all_data, file)

    print("Data saved to data.json")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")