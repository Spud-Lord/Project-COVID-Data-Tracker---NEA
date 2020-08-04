#Jake Eaton

from creategdpgraph import GDPGraph
from createinflationgraph import InflationGraph
from createinfectiongraph import InfectionGraph #Imports functions from programs
from createdeathgraph import DeathGraph
from typing import type, type2
import time #Imports time module

def Nav():
    type("Would you like to view a Financial Graph or COVID-19 Data Graph? Type Exit to go back\n")
    choice = input("")
    print("")

    if choice.lower() == "financial":
        type("Would you like to view GDP or Inflation?")
        fgraphtype = input("")

        if fgraphtype.lower() == "gdp":
            GDPGraph()

        elif fgraphtype.lower() == "inflation":
            InflationGraph()

    elif choice.lower() == "covid-19":
        type("Would you like to view Infection or Death numbers?")
        cgraphtype = input("")

        if cgraphtype.lower() == "infection":
            InfectionGraph()

        elif cgraphtype.lower() == "death":
            DeathGraph()

    elif choice.lower() == "exit":
        print("To be Added")

    else:
        type("Please choose one of the options above")
        time.sleep(2)
