#Country Specific Request API Test

import requests

url = requests.get("https://api.covid19api.com/country/south-africa/status/confirmed")

print(url.content)
