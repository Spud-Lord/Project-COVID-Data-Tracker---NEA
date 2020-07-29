#Jake Eaton


import requests

def Call():
    country = country.lower()
    url = requests.get("https://api.covid19api.com/country/"+country+"/status/confirmed")
    print(country.content)
