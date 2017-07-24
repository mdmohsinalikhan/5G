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
#plt.plot(x, 1000*(1 - (1 - 1/10**10)**x), linewidth=1, linestyle="-", c="black", alpha = 1);
#plt.plot(x, 10000*(1 - (1 - 1/10**10)**x), linewidth=1, linestyle="-", c="red", alpha = 1);
#plt.plot(x, 100000*(1 - (1 - 1/10**10)**x), linewidth=1, linestyle="-", c="green", alpha = 1);

plt.plot(x, 1000*x/(10**10), linewidth=5, linestyle="--", c="black", alpha = 1, label = "$r = 10^3$");
plt.plot(x, 10000*x/(10**10), linewidth=5, linestyle=":", c="black", alpha = 1, label = "$r = 10^4$");
plt.plot(x, 100000*x/(10**10), linewidth=5, linestyle="-", c="black", alpha = 1, label = "$r = 10^5$");


plt.rcParams.update({'font.size': 50})
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))



#Formatting the plot
plt.xlabel('#Pseudonyms ($m$)')
plt.ylabel('#Affected Users ($rm/\mathcal{M}$)')
plt.yticks(np.arange(0, 11, 2))
plt.xticks(np.arange(0, 10**6+1, 2*10**5))
leg = plt.legend(fancybox=True, bbox_to_anchor=(.6, 1))
leg.get_frame().set_alpha(0.5)
plt.grid()
plt.show()

