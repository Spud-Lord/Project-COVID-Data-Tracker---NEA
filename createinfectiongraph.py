#Jake Eaton

from callinfectionfunction import CountryCall
from dataformatter import Formatter
import matplotlib.pyplot as plt

def InfectionGraph():
    url = CountryCall()
    #format of data = [[country,countrycode,province,city,citycode,latitude,longitude,cases,status,date][next batch of data]
    #then getting the data is easy
    #and dont worry, i promise all the variable names are normal and nothing is an insult to myself or the code.
    Sorted = Formatter(url.content)

    x =[]
    y =[]

    for i in range(len(Sorted)):
        val =Sorted[i][9]
        x.append(val[:10])
        y.append(Sorted[i][7])

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")
    ax.set(xlabel="Date", ylabel="Number of Infections", title="Switzerland Test")
    plt.xticks(rotation = 90)#we are rotating the labels so we can read them
    plt.show()
