#Call All Data Test

<<<<<<< Updated upstream
import requests

url = "https://api.covid19api.com/all"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
=======
response = requests.get("https://api.covid19api.com/all")
print(response.content)
>>>>>>> Stashed changes
