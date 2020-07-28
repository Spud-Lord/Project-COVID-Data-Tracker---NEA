#MatPlotLib Test

import matplotlib.pyplot as plt
# plt.plot([1, 2, 3, 4]) #What to plot
# plt.ylabel('some numbers') #Label for Y Axis
# plt.show() #Show Graph

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16]) #Plot for X and Y - X is first array, Y is second Array
# plt.ylabel('some numbers') #Label for Y Axis
# plt.show() #Show Graph

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') #Plot for X and Y - X is first array, Y is second arrat, ro makes the dots round
# plt.axis([0, 6, 0, 20]) #Lists the axis numbers - The first two are for the X Axis, the second two are for the Y Axis
# plt.show() #Show Graph

# names = ['group_a', 'group_b', 'group_c'] #States Name for different graphs
# values = [1, 10, 100] #Sets values for points
#
# plt.figure(figsize=(9, 3)) #States size of graphs
#
# plt.subplot(131)
# plt.bar(names, values) #Plots a bar graph with names and values
# plt.subplot(132)
# plt.scatter(names, values) #Plots a scatter graph with names and values
# plt.subplot(133)
# plt.plot(names, values) #Plots a line graph with names and values
# plt.suptitle('Categorical Plotting') #Nmae of document
# plt.show() #Show Graph
