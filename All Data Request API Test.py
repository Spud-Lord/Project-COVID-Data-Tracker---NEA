#Call All Data Test

import requests

url = "https://api.covid19api.com/all"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
