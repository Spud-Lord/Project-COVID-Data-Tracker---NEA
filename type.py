#Jake Eaton
#Type Code

import sys, time                    #Imports System and Time Modules

def type(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()          #This def will print strings in this way. When type is used instead of print, the program will now know to print each character separately with a tiny time gap inbetween
        time.sleep(0.04)
    sys.stdout.write("\n")
