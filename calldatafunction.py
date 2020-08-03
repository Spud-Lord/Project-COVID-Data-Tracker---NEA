#Jake Eaton

from typing import type, type2
import requests

def CountryCall():
    type("What country do you want data from? For countries with multiple words in their name, put a - inbetween each word e.g Write South Africa as South-Africa")
    country = input("")
    country = country.lower()
    url = requests.get("https://api.covid19api.com/country/"+country+"/status/confirmed")
    print(url.content)
