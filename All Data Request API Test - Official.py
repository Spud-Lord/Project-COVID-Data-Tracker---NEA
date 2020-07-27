#Call All Data Test

<<<<<<< HEAD
=======
<<<<<<< Updated upstream
>>>>>>> d933918fd35bf5a80e56000d3016191f48cbfe7b
import requests

url = "https://api.covid19api.com/all"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
<<<<<<< HEAD
=======
=======
response = requests.get("https://api.covid19api.com/all")
print(response.content)
>>>>>>> Stashed changes
>>>>>>> d933918fd35bf5a80e56000d3016191f48cbfe7b
