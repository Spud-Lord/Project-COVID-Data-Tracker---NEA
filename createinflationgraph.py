#Jake Eaton

from calldatafunction import CountryCall #Imports functions from programs
import matplotlib.pyplot as plt #Imports MatPlotLib Module

def InflationGraph():
    CountryCall()

    x = []
    y = []

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")
    ax.set(xlabel="Date", ylabel="Inflation Rate", title="Switzerland Test")
    plt.show()
