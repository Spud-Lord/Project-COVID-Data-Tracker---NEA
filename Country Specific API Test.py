#Country Specific Request API Test

import requests

url = "https://api.covid19api.com/country/south-africa/status/confirmed"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
