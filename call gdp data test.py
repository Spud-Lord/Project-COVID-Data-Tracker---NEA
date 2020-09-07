#Jake createinfectiongraph
import requests

url = requests.get("http://api.worldbank.org/v2/country/br/indicator/NY.GDP.MKTP.CD?date=2006")
print(url.content)
