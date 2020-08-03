#Jake Eaton

from calldatafunction import CountryCall
import matplotlib.pyplot as plt

def InflationGraph():
    CountryCall()

    x = []
    y = []

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue",s=2)
    ax.set(xlabel="", ylabel="Inflation Rate", title=country)
    plt.show()
