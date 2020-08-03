#Jake Eaton

from calldatafunction import CountryCall
import matplotlib.pyplot as plt

def DeathGraph():
    CountryCall()

    x = [Date]
    y = [Deaths]

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")
    ax.set(xlabel="Date", ylabel="Number of Deaths", title=country)
    plt.show()
