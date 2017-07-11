import random
import datetime

#imports for plotting
import numpy as np
from matplotlib import pyplot as plt
import math


filename1 = "10_1000000.txt"
filename2 = "10_10000000.txt"

IMSI_space = 10**10


plotlist_x = list()
plotlist_y = list()

bot_size = 0
m = 0

x = np.linspace(0, 10**6, 100000)
plt.plot(x, 100*(1.0-(1.0-1.0/IMSI_space)**(x*2*3600*2) - (x*2*3600*2)*(1.0/IMSI_space)*(1.0-1.0/IMSI_space)**(x*2*3600*2-1.0)), linewidth=1, linestyle="-", c="black", alpha = 1, label = "2 hours");
plt.plot(x, 100*(1.0-(1.0-1.0/IMSI_space)**(x*4*3600*2) - (x*4*3600*2)*(1.0/IMSI_space)*(1.0-1.0/IMSI_space)**(x*4*3600*2-1.0)), linewidth=1, linestyle="-", c="blue", alpha = 1, label = "2 hours");
plt.plot(x, 100*(1.0-(1.0-1.0/IMSI_space)**(x*6*3600*2) - (x*6*3600*2)*(1.0/IMSI_space)*(1.0-1.0/IMSI_space)**(x*6*3600*2-1.0)), linewidth=1, linestyle="-", c="red", alpha = 1, label = "2 hours");
	
#Formatting the plot
plt.xlabel('Number of bots')
plt.ylabel('No of affected users (percentage)')
#plt.title('Success rate of the DoS attack \n' + "IMSI Length: " + str(IMSI_length) + " digits")
#plt.yticks(np.arange(0, 100, 5))
plt.xticks(np.arange(0, 10**6+1, 200000))
plt.grid()
plt.show()

