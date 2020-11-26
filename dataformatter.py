def Formatter(data):
    data = str(data)    #Sets a variable for string data
    SortedData = [] #Array for the final sorted data
    quotes = 0
    important = False   #Sets the boolean important as False
    word = ""   #Sets word as blank
    
    for i in range(len(data)):  #For loop to set data batches
        if data[i] == "{":#New data batch
            batch = []  #Sets array called batch

        elif data[i] == "}":#End of batch
            SortedData.append(batch)    #Adds the batch data to the Sorted Data Array


        if  important == False and data[i] == ":":
           important  = True    #Sets boolean important as True if the requirements are met

        elif important == True:
            if data[i] == ",":
                important = False   #Sets boolean important as False if the requirements are met

                if word == "":
                    word = None #If word is blank then set the word variable as nothing

                try:
                    word = float(word)  #If the above is not met then try to make the variable word as a float

                except:
                    pass    #If nothing is met then pass it

                try:
                    word = int(word)    #Try making word an integer

                except:
                    pass    #Pass it if not met

                batch.append(word)  #Appends the batch Array with the word variable
                word = ""   #Sets word to be blank

            else:
                if data[i] != '"':
                    word = word + data[i]   #Sets word variable to be word with the data[i] added to the end

    del SortedData[len(SortedData)-1]   #Deletes Sorted Data Array for those with length of Sorted Array being one less
    return SortedData   #Returns the Sorted Data Array
