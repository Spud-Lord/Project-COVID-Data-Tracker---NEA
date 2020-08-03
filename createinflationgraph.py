#Jake Eaton

from calldatafunction import CountryCall
import matplotlib.pyplot as plt

def InflationGraph():
    CountryCall()

    x = []
    y = []

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")
    ax.set(xlabel="Date", ylabel="Inflation Rate", title=country)
    plt.show()
