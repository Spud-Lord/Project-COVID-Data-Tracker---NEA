#Jake Eaton

from calldeathfunction import CountryCall
from dataformatter import Formatter #Imports functions from programs
import matplotlib.pyplot as plt #Imports MatPlotLib Module

def DeathGraph():
    url = CountryCall() #Sets the CountryCall Function as a variable
    sorted = Formatter(url.content) #Sets the data gathered from the API as a variable

    x = []  #Blank arrays for the X and Y Axis Data
    y = []

    for i in range(len(sorted)):    #For loop to put the data in the appropriate axes
        val = sorted[i][9]  #The values are from the Sorted array
        x.append(val[:10])  #Make the x-axis the val variable
        y.append(sorted[i][7])  #Make the y-axis the sorted variable

    fig, ax = plt.subplots()    #Plot the plots on a graph
    plt.plot(x,y,color="blue")  #Plots X and Y in colour blue
    ax.set(xlabel="Date", ylabel="Number of Deaths")    #Sets the labels of the axes
    plt.xticks(rotation = 90)   #Rotates the labels to be orientated to be readable
    plt.draw()  #Draws Graph but does NOT show it
