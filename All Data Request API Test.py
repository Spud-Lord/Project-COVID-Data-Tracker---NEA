#Call All Data Test

import requests

url = requests.get("https://api.covid19api.com/all")

print(url.content)
