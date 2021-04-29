#Jake Eaton

from callinfectionfunction import CountryCall
from dataformatter import Formatter #Imports functions from programs
import matplotlib.pyplot as plt #Imports MatPlotLib Module

def InfectionGraph():
    url = CountryCall() #Sets the CountryCall Function as a variable
    Sorted = Formatter(url.content) #Sets the data gathered from the API as a variable

    x = []  #Blank arrays for the X and Y Axis Data
    y = []

    for i in range(len(Sorted)):    #For loop to put the data in the appropriate axes
        val = Sorted[i][9]  #The values are from the Sorted array
        x.append(val[:10])  #Make the x-axis the val variable
        y.append(Sorted[i][7])  #Make the y-axis the sorted variable

    fig, ax = plt.subplots()
    plt.plot(x,y,color="blue")  #Plots X and Y in colour blue
    ax.set(xlabel="Date", ylabel="Number of Infections", title="Test")    #Sets the labels of the axes
    plt.xticks(rotation = 90)   #Rotates the labels to be orientated to be kind of readable
    plt.draw()  #Draws Graph but does NOT show it
