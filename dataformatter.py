def Formatter(data):
    data = str(data)
    #we got our data lets solve it now
    SortedData = [] #for the end result
    quotes = 0 #trust me we need this it will make life easy
    important = False
    word = ""
    for i in range(len(data)):
        if data[i] == "{":#new data batch
            batch = []
        elif data[i] == "}":#end of batch
            #print(batch)
            SortedData.append(batch)


        if  important == False and data[i] == ":":
           important  = True

        elif important == True:
            if data[i] == ",":
                important = False
                if word == "":
                    word = None
                try:
                    word = float(word)
                except:
                    pass
                try:
                    word = int(word)
                except:
                    pass
                #print(word)
                batch.append(word)
                word = ""
            else:
                if data[i] != '"':
                    word = word + data[i]

    #print(SortedData) #we got it bois this is sorted beautiful data, im hella proud
    del SortedData[len(SortedData)-1]
    return SortedData
