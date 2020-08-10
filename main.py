#Jake Eaton
#Project Zeta Data

from creategdpgraph import GDPGraph
from createinflationgraph import InflationGraph
from createinfectiongraph import InfectionGraph #Imports functions from programs
from createdeathgraph import DeathGraph
from typing import type, type2
import time #Imports time module

type("Welcome!\n")
time.sleep(2)
def Menu():
    type("Would you like to view a Financial Graph or COVID-19 Data Graph? Type Exit to quit the program\n")
    choice = input("")  #Sets the user input as the variable choice
    print("")   #Prints a gap to neaten the view

    if choice.lower() == "financial":   #Sets the user input as lower case to avoid any capital letter mistakes
        type("Would you like to view GDP or Inflation?\n")
        fgraphtype = input("")
        print("")   #Prints a gap to neaten the view

        if fgraphtype.lower() == "gdp":   #Sets the user input as lower case to avoid any capital letter mistakes
            GDPGraph()  #Runs Function
            print("")   #Prints a gap to neaten the view
            Menu()

        elif fgraphtype.lower() == "inflation":   #Sets the user input as lower case to avoid any capital letter mistakes
            InflationGraph()  #Runs Function
            print("")   #Prints a gap to neaten the view
            Menu()

    elif choice.lower() == "covid-19":   #Sets the user input as lower case to avoid any capital letter mistakes
        type("Would you like to view Infection or Death numbers?\n")
        cgraphtype = input("")

        if cgraphtype.lower() == "infection":   #Sets the user input as lower case to avoid any capital letter mistakes
            InfectionGraph()  #Runs Function
            print("")   #Prints a gap to neaten the view
            Menu()

        elif cgraphtype.lower() == "death":   #Sets the user input as lower case to avoid any capital letter mistakes
            DeathGraph()  #Runs Function
            print("")   #Prints a gap to neaten the view
            Menu()

    elif choice.lower() == "exit":   #Sets the user input as lower case to avoid any capital letter mistakes
        exit()

    else:
        type("Please choose one of the options above")
        time.sleep(2)
Menu()
