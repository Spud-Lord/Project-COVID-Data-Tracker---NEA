#Jake Eaton

import requests
import matplotlib.pyplot as plt

country = input("What country do you want data from? ")
country = country.lower()
url = requests.get("http://api.covid19api.com/country/"+country+"/status/confirmed")

plt.plot(url.date, url.cases)
plt.ylabel("Number of Cases")
plt.xlabel("Date")
plt.show()
