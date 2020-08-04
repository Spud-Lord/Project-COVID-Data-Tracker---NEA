#Jake Eaton

from calldatafunction import CountryCall    #Imports required functions
import matplotlib.pyplot as plt #Imports MatPlotLib as plot

def DeathGraph():
    CountryCall()

    x = [Date]
    y = [Deaths]

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")
    ax.set(xlabel="Date", ylabel="Number of Deaths", title="Switzerland Test")
    plt.show()
