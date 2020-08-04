#Jake Eaton

from creategdpgraph import GDPGraph
from createinflationgraph import InflationGraph
from createinfectiongraph import InfectionGraph #Imports functions from programs
from createdeathgraph import DeathGraph
from typing import type, type2
import time #Imports time module

def Nav():
    type("Would you like to view a Financial Graph or COVID-19 Data Graph? Type Exit to go back\n")
    choice = input("")  #Sets the user input as the variable choice
    print("")   #Prints a gap to neaten the view

    if choice.lower() == "financial":   #Sets the user input as lower case to avoid any capital letter mistakes
        type("Would you like to view GDP or Inflation?")
        fgraphtype = input("")

        if fgraphtype.lower() == "gdp":   #Sets the user input as lower case to avoid any capital letter mistakes
            GDPGraph()  #Runs Function

        elif fgraphtype.lower() == "inflation":   #Sets the user input as lower case to avoid any capital letter mistakes
            InflationGraph()  #Runs Function

    elif choice.lower() == "covid-19":   #Sets the user input as lower case to avoid any capital letter mistakes
        type("Would you like to view Infection or Death numbers?")
        cgraphtype = input("")

        if cgraphtype.lower() == "infection":   #Sets the user input as lower case to avoid any capital letter mistakes
            InfectionGraph()  #Runs Function

        elif cgraphtype.lower() == "death":   #Sets the user input as lower case to avoid any capital letter mistakes
            DeathGraph()  #Runs Function

    elif choice.lower() == "exit":   #Sets the user input as lower case to avoid any capital letter mistakes
        print("To be Added")

    else:
        type("Please choose one of the options above")
        time.sleep(2)
