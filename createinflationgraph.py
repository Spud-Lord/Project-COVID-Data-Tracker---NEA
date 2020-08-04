#Jake Eaton

from calldatafunction import CountryCall    #Imports required functions
import matplotlib.pyplot as plt #Imports MatPlotLib as plot

def InflationGraph():
    CountryCall()

    x = []
    y = []

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")
    ax.set(xlabel="Date", ylabel="Inflation Rate", title="Switzerland Test")
    plt.show()
