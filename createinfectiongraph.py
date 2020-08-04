#Jake Eaton

from calldatafunction import CountryCall    #Imports required functions
import matplotlib.pyplot as plt #Imports MatPlotLib as plot

def InfectionGraph():
    CountryCall()

    x = [url.Date]
    y = [url.Cases]

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")
    ax.set(xlabel="Date", ylabel="Number of Infections", title="Switzerland Test")
    plt.show()
