import requests
import json
import os

class AirportApiClient():
    def __init__(self):
        pass

    async def get(self,endpoint):
        url = os.getenv("API_BASE_URL") + endpoint
        headers = {
        'Accept': 'application/json'
        }
        response = requests.request("GET", url, headers=headers)

        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception("Error: " + str(response.status_code) - "Could not retrieve data")