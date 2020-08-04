#Jake Eaton

from calldeathfunction import CountryCall
from dataformatter import Formatter
import matplotlib.pyplot as plt

def DeathGraph():
    url = CountryCall()
    sorted = Formatter(url.content)

    x = []
    y = []

    for i in range(len(sorted)):
        val = sorted[i][9]
        x.append(val[:10])
        y.append(sorted[i][7])

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")
    ax.set(xlabel="Date", ylabel="Number of Deaths", title="Switzerland Test")
    plt.xticks(rotation = 90)
    plt.show()
