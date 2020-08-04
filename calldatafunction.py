#Jake Eaton

from typing import type, type2  #Import required functions
import requests #Imports Requests Module

def CountryCall():
    type("What country do you want data from? For countries with multiple words in their name, put a - inbetween each word e.g Write South Africa as South-Africa")
    country = input("")
    country = country.lower()   #Converts the input to be lower case
    url = requests.get("https://api.covid19api.com/country/"+country+"/status/confirmed")   #URL to get confirmed cases in a country
    print(url.content)  #Prints the data that has been collected from the API
