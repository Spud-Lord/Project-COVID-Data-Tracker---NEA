#Jake Eaton

from calldatafunction import CountryCall #Imports functions from programs
import matplotlib.pyplot as plt #Imports MatPlotLib Module

def GDPGraph():
    CountryCall()

    x = []
    y = []

    fig, ax = plt.subplots()
    plt.plot(x, y, color="blue")
    ax.set(xlabel="Date", ylabel="Gross Domestic Product", title="Switzerland Test")
    plt.show()
