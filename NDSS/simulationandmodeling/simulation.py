import random
import datetime

#imports for plotting
import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import math

IMSI_length = 8
IMSI_space = 10**IMSI_length

attacklength = 2*10**IMSI_length
readings_with_replacement = 50
readinginterval = attacklength/readings_with_replacement
no_of_rounds_with_replacement = 1


attacklength_without_replacement = 2*10**IMSI_length
readings_without_replacement = 50
readinginterval_without_replacement = attacklength_without_replacement/readings_without_replacement
no_of_rounds_without_replacement = 1

plotlist_x = list()
plotlist_y = list()

no_of_subscribers = 10**6
used_IMSIs = set()
pseudonymsp1 = dict()
pseudonymsp2 = dict()
initialconfig = dict()
currentconfig = dict()
attacktracker = dict()
result_of_with_replacement = dict()
result_of_without_replacement = dict()


def HN_functionality(guessed_pseudonym):
		if guessed_pseudonym in pseudonymsp2:
		#make the guessed pseudonym p1
			IMSI = pseudonymsp2[guessed_pseudonym]
			p1 = pseudonymsp1[IMSI]
			pseudonymsp1[IMSI] = guessed_pseudonym
		#remove p1 from the used pool
			used_IMSIs.discard(p1)
		#remove the gussed pseudonym from bein p2
			pseudonymsp2.pop(guessed_pseudonym)
		#generate a new pseudonym from unused pool and set it as p2
			pseudonym = random_unused_IMSI()
			pseudonymsp2[pseudonym] = IMSI
		#update current config
			#currentconfig[IMSI] = guessed_pseudonym + " " + pseudonym
		#update attacktracker
			attacktracker[IMSI] = attacktracker[IMSI] + 1

def record_result_of_with_replacement(i):
			count = 0
			for j in attacktracker:
				if attacktracker[j] > 1:
					count = count + 1
			if i in result_of_with_replacement:
				result_of_with_replacement[i] = result_of_with_replacement[i] + ":" + str(count)
			else:
				result_of_with_replacement[i] = str(count)

def record_result_of_without_replacement(i):
			count = 0
			for j in attacktracker:
				if attacktracker[j] > 1:
					count = count + 1
			if i in result_of_without_replacement:
				result_of_without_replacement[i] = result_of_without_replacement[i] + ":" + str(count)
			else:
				result_of_without_replacement[i] = str(count)
	


def attack_with_replacement():
	for i in range(0,attacklength):
		guessed_pseudonym = random_IMSI()
		HN_functionality(guessed_pseudonym)
		if (i+1)%1000000 == 0:
			print(str(datetime.datetime.utcnow()) + ": Already guessed: " + str((i+1)/1000000) + " million")
		if (i+1)%readinginterval == 0:
			record_result_of_with_replacement(i+1)			
			


def attack_without_replacement():
	for i in range(0,10**IMSI_length): 
		guessed_pseudonym = str(i).zfill(IMSI_length)
		HN_functionality(guessed_pseudonym)
		if (i+1)%1000000 == 0:
			print(str(datetime.datetime.utcnow()) + ": Already guessed: " + str((i+1)/1000000) + " million")
		if (i+1)%readinginterval_without_replacement == 0:
			record_result_of_without_replacement(i+1)

	for i in range(0,10**IMSI_length): 
		guessed_pseudonym = str(i).zfill(IMSI_length)
		HN_functionality(guessed_pseudonym)
		if (i+1)%1000000 == 0:
			print(str(datetime.datetime.utcnow()) + ": Already guessed: " + str((10**IMSI_length+i+1)/1000000) + " million")
		if (10**IMSI_length+i+1)%readinginterval_without_replacement == 0:
			record_result_of_without_replacement(10**IMSI_length+i+1)

def random_unused_IMSI():
	while 5 == 5:
		IMSI = ""	
		for i in range(0,IMSI_length):
			IMSI = IMSI + ''.join(random.sample(['1', '2', '3', '4', '5','6','7','8','9','0'],1))

		
		if IMSI not in used_IMSIs:
			used_IMSIs.add(IMSI)
			break

	return IMSI


def random_IMSI():
	IMSI = ""	
	for i in range(0,IMSI_length):
		IMSI = IMSI + ''.join(random.sample(['1', '2', '3', '4', '5','6','7','8','9','0'],1))

	return IMSI


def create_users():
	print(str(datetime.datetime.utcnow()) + ": Creating Users")
	for i in range(0,no_of_subscribers):
		#generate a new IMSI from unused pool
		IMSI = random_unused_IMSI()
		attacktracker[IMSI] = 0

		#generate a pseudonym p1 from unused pool
		pseudonym1 = random_unused_IMSI()
		pseudonymsp1[IMSI] = pseudonym1 

		#generate a pseudonym p2 from unused pool
		pseudonym2 = random_unused_IMSI()
		pseudonymsp2[pseudonym2] = IMSI 

		#record the inital config and current config
		#initialconfig[IMSI] = pseudonym1 + " " + pseudonym2
		#currentconfig[IMSI] = pseudonym1 + " " + pseudonym2

def initializeattack():
	used_IMSIs.clear()
	pseudonymsp1.clear()
	pseudonymsp2.clear()
	initialconfig.clear()
	currentconfig.clear()
	attacktracker.clear()
	create_users()

def plot_everything():
	for i in range(0,no_of_rounds_with_replacement):
		plotlist_x[:] = []
		plotlist_y[:] = []
		for j in sorted(result_of_with_replacement):
			plotlist_y.append(result_of_with_replacement[j].split(":",no_of_rounds_with_replacement)[i])
			plotlist_x.append(j)
		plt.plot(plotlist_x, plotlist_y, linewidth=1, linestyle="-", c="red", alpha = 1)

	for i in range(0,no_of_rounds_without_replacement):
		plotlist_x[:] = []
		plotlist_y[:] = []
		for j in sorted(result_of_without_replacement):
			plotlist_y.append(result_of_without_replacement[j].split(":",no_of_rounds_without_replacement)[i])
			plotlist_x.append(j)
		plt.plot(plotlist_x, plotlist_y, linewidth=1, linestyle="-", c="green", alpha = 1,)


	x = np.linspace(0, attacklength, attacklength)
	plt.plot(x, no_of_subscribers*(1.0-(1.0-1.0/IMSI_space)**x - x*(1.0/IMSI_space)*(1.0-1.0/IMSI_space)**(x-1.0)), linewidth=3, linestyle="-", c="black", alpha = .25);


	#Formatting the plot
	plt.xlabel('Number of guessed pseudonyms')
	plt.ylabel('No of affected users')
	plt.title('Success rate of the DoS attack \n' + "IMSI Lenght: " + str(IMSI_length) + " digits, " + "Number of Subscribers: " + str(no_of_subscribers))
	
	plt.show()


#the main function starts from here

#attack with replacement
for i in range(0,no_of_rounds_with_replacement):
	initializeattack()
	print(str(datetime.datetime.utcnow()) + ": With-replacement attack, round: " + str(i+1) + " has started")
	attack_with_replacement()

#attack without replacement
for i in range(0,no_of_rounds_without_replacement):
	initializeattack()
	print(str(datetime.datetime.utcnow()) + ": Without-replacement attack, round: " + str(i+1) + " has started")
	attack_without_replacement()


#print("Result of with replacement attack:")
#for key in sorted(result_of_with_replacement):
#    print("No of pseudonyms sent: " + str(key) +  " and affected users: " + str(result_of_with_replacement[key]))

#print("Result of without replacement attack:")
#for key in sorted(result_of_without_replacement):
#    print("No of pseudonyms sent: " + str(key) +  " and affected users: " + str(result_of_without_replacement[key]))

plot_everything()




