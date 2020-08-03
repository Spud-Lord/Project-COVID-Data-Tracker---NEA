#Jake Eaton

from calldatafunction import CountryCall
import matplotlib.pyplot as plt

def InfectionGraph():
    CountryCall()

    x = []
    y = []

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")
    ax.set(xlabel="Date", ylabel="Number of Infections", title="Switzerland Test")
    plt.show()
