import requests
import json


url = "https://data..net/v3/-data.json"

payload={}
headers = {
'Accept': 'application/json'
}

response = requests.request("GET", url, headers=headers, data=payload)

res = json.loads(response.text)

print(len(res))