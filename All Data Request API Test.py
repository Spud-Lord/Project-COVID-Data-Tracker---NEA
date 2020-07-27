#Call All Data Test

import requests

response = requests.get("https://api.covid19api.com/all")
print(response.content)
