#Jake Eaton

from creategdpgraph import GDPGraph
from createinflationgraph import InflationGraph
from createinfectiongraph import InfectionGraph #Imports the required functions
from createdeathgraph import DeathGraph
from typing import type, type2
import time #Imports time

def Nav():
    type("Would you like to view a Financial Graph or COVID-19 Data Graph? Type Exit to go back")
    choice = input("")
    print("")

    if choice.lower() == "financial":   #Sets the input to be lower case to avoid any capital letter mistakes
        type("Would you like to view GDP or Inflation?")
        fgraphtype = input("")

        if fgraphtype.lower() == "gdp":   #Sets the input to be lower case to avoid any capital letter mistakes
            GDPGraph()

        elif fgraphtype.lower() == "inflation":   #Sets the input to be lower case to avoid any capital letter mistakes
            InflationGraph()

    elif choice.lower() == "covid-19":   #Sets the input to be lower case to avoid any capital letter mistakes
        type("Would you like to view Infection or Death numbers?")
        cgraphtype = input("")

        if cgraphtype.lower() == "infection":   #Sets the input to be lower case to avoid any capital letter mistakes
            InfectionGraph()

        elif cgraphtype.lower() == "death":   #Sets the input to be lower case to avoid any capital letter mistakes
            DeathGraph()

    elif choice.lower() == "exit":   #Sets the input to be lower case to avoid any capital letter mistakes
        print("To be Added")

    else:
        type("Please choose one of the options above")
        time.sleep(2)
