import random
import datetime

#imports for plotting
import numpy as np
from matplotlib import pyplot as plt
import math

plt.rcParams.update({'font.size': 50})
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

filename1 = "10_1000000.txt"
filename2 = "10_10000000.txt"

IMSI_space = 10**10


plotlist_x = list()
plotlist_y = list()

bot_size = 0
m = 0

x = np.linspace(0, 30, 720)

bot_load = 3
botnet_size = 10**6
m_per_day = 24*bot_load*botnet_size
plt.plot(x, 100*(1.0-(1.0-1.0/IMSI_space)**(x*m_per_day) - (x*m_per_day)*(1.0/IMSI_space)*(1.0-1.0/IMSI_space)**(x*m_per_day-1.0)), linewidth=5, linestyle="-", c="black", alpha = 1, label = "3 pseudonyms/hour");

bot_load = 60
botnet_size = 10**6
m_per_day = 24*bot_load*botnet_size
plt.plot(x, 100*(1.0-(1.0-1.0/IMSI_space)**(x*m_per_day) - (x*m_per_day)*(1.0/IMSI_space)*(1.0-1.0/IMSI_space)**(x*m_per_day-1.0)), linewidth=5, linestyle="--", c="black", alpha = 1, label = "60 pseudonyms/hour");

bot_load = 360
botnet_size = 10**6
m_per_day = 24*bot_load*botnet_size
plt.plot(x, 100*(1.0-(1.0-1.0/IMSI_space)**(x*m_per_day) - (x*m_per_day)*(1.0/IMSI_space)*(1.0-1.0/IMSI_space)**(x*m_per_day-1.0)), linewidth=5, linestyle="-.", c="black", alpha = 1, label = "360 pseudonyms/hour");

bot_load = 3600
botnet_size = 10**6
m_per_day = 24*bot_load*botnet_size
plt.plot(x, 100*(1.0-(1.0-1.0/IMSI_space)**(x*m_per_day) - (x*m_per_day)*(1.0/IMSI_space)*(1.0-1.0/IMSI_space)**(x*m_per_day-1.0)), linewidth=5, linestyle=":", c="black", alpha = 1, label = "3600 pseudonyms/hour");



#Formatting the plot
plt.xlabel('After $d$ Days')
plt.ylabel('Affected Users ($E[u_a] * 100$)')
#plt.title('Success rate of the DoS attack \n' + "IMSI Length: " + str(IMSI_length) + " digits")
plt.yticks(np.arange(0, 100, 10))
plt.xticks(np.arange(0, 30+1, 5))
leg = plt.legend(bbox_to_anchor=(1.2, 1))
leg.get_frame().set_alpha(0.5)
plt.grid()
plt.show()

