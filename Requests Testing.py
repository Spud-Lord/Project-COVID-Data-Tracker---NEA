#Jake Eaton

import requests

country = input("What country do you want data from? ")
country = country.lower()
url = requests.get("https://api.covid19api.com/country/"+country+"/status/confirmed")
print(url.json())
print("")
print(url.headers)
print("")
print(url.headers['content-type'])
