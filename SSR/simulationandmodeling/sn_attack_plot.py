import random
import datetime

#imports for plotting
import numpy as np
from matplotlib import pyplot as plt
import math


def xchoosey(x,y):
	if y == x:
    		return 1
	elif y == 1:         # see georg's comment
    		return x
	elif y > x:          # will be executed only if y != 1 and y != x
    		return 0
	else:                # will be executed only if y != 1 and y != x and x <= y
    		a = math.factorial(x)
    		b = math.factorial(y)
    		c = math.factorial(x-y)  # that appears to be useful to get the correct result
    		div = a // (b * c)
    		return div



#print(str(xchoosey(10**10,10**6)))

x = np.linspace(0, 10**6, 1000)
plt.plot(x, 1000*(1 - (1 - 1/10**10)**x), linewidth=1, linestyle="-", c="black", alpha = 1);
plt.plot(x, 10000*(1 - (1 - 1/10**10)**x), linewidth=1, linestyle="-", c="red", alpha = 1);
plt.plot(x, 100000*(1 - (1 - 1/10**10)**x), linewidth=1, linestyle="-", c="green", alpha = 1);


#Formatting the plot
plt.xlabel('Number Of Pseudonyms guessed (with replacement)')
plt.ylabel('No of affected users ')
#plt.yticks(np.arange(0, 100, 5))
#plt.xticks(np.arange(0, 6*10**10+1, 5*10**9))
plt.grid()
plt.show()

