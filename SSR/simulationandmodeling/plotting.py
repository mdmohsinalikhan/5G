import random
import datetime

#imports for plotting
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.lines as mlines
import math


filename1 = "10_1000000.txt"
filename2 = "10_10000000.txt"

temporary_container_with_replacement = dict()
temporary_container_without_replacement = dict()

plotlist_x = list()
plotlist_y = list()



IMSI_length = 0
attack_length_with_replacement = 0
no_of_subscribers = 0
no_of_readings_with_replacement = 0
no_of_rounds_with_replacement = 0
attacklength_without_replacement = 0
no_of_readings_without_replacement = 0
no_of_rounds_without_replacement = 0
IMSI_space = 0
style = ":"


def plot(k):
	if k == 1:
		#for i in range(0,no_of_rounds_with_replacement):
		for i in range(0,1):
			plotlist_x[:] = []
			plotlist_y[:] = []
			for j in range(0,no_of_readings_with_replacement):
				plotlist_y.append(100*(float(temporary_container_with_replacement[j].split(":",no_of_rounds_with_replacement)[i+1]))/no_of_subscribers)
				plotlist_x.append(temporary_container_with_replacement[j].split(":",no_of_rounds_with_replacement)[0])
		
			plt.plot(plotlist_x, plotlist_y, ':', linewidth=10, c="black", alpha = 1, label = "With Replcmnt (simltn)")
			#print(plotlist_x)


		#for i in range(0,no_of_rounds_without_replacement):
		for i in range(0,1):
			plotlist_x[:] = []
			plotlist_y[:] = []
			for j in range(0,no_of_readings_without_replacement):
				plotlist_y.append((100*float(temporary_container_without_replacement[j].split(":",no_of_rounds_without_replacement)[i+1]))/no_of_subscribers)
				plotlist_x.append(temporary_container_without_replacement[j].split(":",no_of_rounds_without_replacement)[0])
		
			plt.plot(plotlist_x, plotlist_y, '-.', linewidth=10, c="black", alpha = 1, label = "Without Replcmnt (simltn)")
	

		x = np.linspace(0, attack_length_with_replacement, 1000)
		plt.plot(x, 100*(1.0-(1.0-1.0/IMSI_space)**x - x*(1.0/IMSI_space)*(1.0-1.0/IMSI_space)**(x-1.0)), linewidth=5, linestyle="-", c="black", alpha = 1, label = "With Replcmnt (model)");

		x = np.linspace(0, attacklength_without_replacement/2, 500)
		plt.plot(x, 100*(1/10.0**IMSI_length)*((x**2.0)/(2.0*10**IMSI_length)), linewidth=5, linestyle="--", c="black", alpha = 1, label = "Without Replcmnt (model)");

		x = np.linspace(attacklength_without_replacement/2, attacklength_without_replacement, 500)
		plt.plot(x, 100*(1/10.0**IMSI_length)*(2*x - 10**IMSI_length - (x**2.0)/(2.0*10**IMSI_length)), linewidth=5, linestyle="--", c="black", alpha = 1);


def initialize_plotting_data_structures():
	temporary_container_with_replacement.clear()
	temporary_container_without_replacement.clear()


#the main function starts from here
for i in range(1,2):
	
	initialize_plotting_data_structures()

	if i == 1: 
		filename = filename1
	elif i == 2:
		filename = filename2

	f = open(filename, 'r')	


	IMSI_length = int(f.readline().rstrip("\n").split(":")[1])
	attack_length_with_replacement = int(f.readline().rstrip("\n").split(":")[1])
	no_of_subscribers = int(f.readline().rstrip("\n").split(":")[1])
	no_of_readings_with_replacement = int(f.readline().rstrip("\n").split(":")[1])
	no_of_rounds_with_replacement = int(f.readline().rstrip("\n").split(":")[1])
	attacklength_without_replacement = int(f.readline().rstrip("\n").split(":")[1])
	no_of_readings_without_replacement = int(f.readline().rstrip("\n").split(":")[1])
	no_of_rounds_without_replacement = int(f.readline().rstrip("\n").split(":")[1])

	
	IMSI_space = 10**IMSI_length


	print("IMSI lenght: " + str(IMSI_length))
	print("Attack length with replacment: " + str(attack_length_with_replacement))
	print("No of subscribers: " + str(no_of_subscribers))
	print("No of readings with replacement: " + str(no_of_readings_with_replacement))
	print("No of rounds with replacement: " + str(no_of_rounds_with_replacement))
	print("Attack length without replacement: " + str(attacklength_without_replacement))
	print("No of readings without replacement: " + str(no_of_readings_without_replacement))
	print("No of rounds without replacement: " + str(no_of_rounds_without_replacement))
	f.readline()
	for j in range(0,no_of_readings_with_replacement):
		temporary_container_with_replacement[j] = f.readline().rstrip("\n")
	f.readline()
	for j in range(0,no_of_readings_with_replacement):
		temporary_container_without_replacement[j] = f.readline().rstrip("\n")
	f.close()

	print(len(temporary_container_with_replacement))
	print(len(temporary_container_without_replacement))

	plot(i)


plt.rcParams.update({'font.size': 50})
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))



#Formatting the plot
plt.xlabel('Number of Pseudonyms ($m$)')
plt.ylabel('Affected Users ($E[u_a] * 100$)')
plt.yticks(np.arange(0, 100, 15))
plt.xticks(np.arange(0, 6*10**10+1, 10**10))
leg = plt.legend(fancybox=True, bbox_to_anchor=(1.2, 1))
leg.get_frame().set_alpha(0.5)
plt.grid()
plt.show()

