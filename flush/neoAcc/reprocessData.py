# sudo apt-get install python-matplotlib
# 

from neo import Accel # import accelerometer
from time import sleep # to add delays

import string
import time
import os
import sys, getopt
import math
from time import gmtime, strftime

import numpy as np
import matplotlib.pyplot as plt

	
#########################
directory = ""
filepath = ""
delay = 0.05
cycles = 500
windowSize = 20
magnitudeTh = 300
########################

data = list()


def main(argv):
	global filepath, magnitudeTh, windowSize
	try:
		opts, args = getopt.getopt(argv,"f:t:w:",["file=","th=","winsize="])
	except getopt.GetoptError:
		print 'test.py -f <filepath> -t <thereshold> -w <sliding win size>'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-f"):
			filepath = directory + str(arg)
		elif opt in ("-t"):
			magnitudeTh = int(arg)
		elif opt in ("-w"):
			windowSize = int(arg)



def dot():
	sys.stdout.write('.')
	sys.stdout.flush()

def openCsvFile():
	global data, filepath
	print "Trying to open file " + filepath
	with open(filepath, "r") as f:
		data = f.readlines()
	data = [x.strip() for x in data] 

def addValueToCsv(value, file):
	file.write(value + "\n")
	
def addValueToVector(value, vector):
	vector.append(value)
	
def updateWindow(value):
	global window
	window.append(value)	
	if len(window) > windowSize:
		window.pop(0)
		
def getMovementIndex(vector):
	count = 0
	for x in vector:
		if x > magnitudeTh:
			count = count + 1
	return count



main(sys.argv[1:])

openCsvFile()

values = list()

for da in data:
	values.append(int(da))

movementIndex = list()
window = list()

for i in range(0, len(values)): # Run forever
	try:
		updateWindow(values[i])
		movementIndex.append(getMovementIndex(window)) 
	except (KeyboardInterrupt, SystemExit):
		dataFile.flush()
		sys.exit()

plt.title(filepath)
plt.subplot(211)
plt.plot(values)
plt.ylabel('acceleration magnitude')

plt.subplot(212)
plt.plot(movementIndex)

plt.show()
