#Jake Eaton

from calldeathfunction import CountryCall #Imports functions from programs
from dataformatter import Formatter
import matplotlib.pyplot as plt #Imports MatPlotLib Module

def DeathGraph():
    url = CountryCall() #Sets the CountryCall Function as a variable
    sorted = Formatter(url.content) #Sets the data gathered from the API as a variable

    x = []  #Blank arrays for the X and Y Axis Data
    y = []

    for i in range(len(sorted)):    #For loop to put the data in the appropriate axes
        val = sorted[i][9]
        x.append(val[:10])
        y.append(sorted[i][7])

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")  #Plots X and Y in colour blue
    ax.set(xlabel="Date", ylabel="Number of Deaths")    #Sets the labels of the axes
    plt.xticks(rotation = 90)   #Rotates the labels to be orientated to be readable
    plt.show()  #Shows Graph
