#Jake Eaton

from calldatafunction import CountryCall
import matplotlib.pyplot as plt

def GDPGraph():
    CountryCall()

    x = []
    y = []

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue",s=2)
    ax.set(xlabel="", ylabel="Gross Domestic Product", title=country)
    plt.show()
