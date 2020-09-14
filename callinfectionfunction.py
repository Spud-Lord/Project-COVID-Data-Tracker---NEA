#Jake Eaton

from typing import type, type2 #Imports functions from programs
import requests #Imports Requests Module

def CountryCall():
    print("")
    type("What country do you want data from? For countries with multiple words in their name, put a - inbetween each word e.g Write South Africa as South-Africa\n")
    country = input("")
    country = country.lower()   #Converts the input to be lower case
    url = requests.get("https://api.covid19api.com/country/"+country+"/status/confirmed")   #URL to get confirmed cases in a country
    return url
