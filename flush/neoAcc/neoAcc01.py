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
directory = "data/"
outFilename = ""
delay = 0.05
cycles = 500
########################

def main(argv):
	global delay
	global cycles
	try:
		opts, args = getopt.getopt(argv,"d:c:",["delay=","cycles="])
	except getopt.GetoptError:
		print 'test.py -d <seconds> -c <number_of_samples>'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-d", "--delay"):
			delay = float(arg)
		elif opt in ("-c", "--cycles"):
			cycles = int(arg)
	print 'Frequency (Hz): ' + str(1/float(delay))
	print 'Cycles: ' + str(cycles)


def dot():
	sys.stdout.write('.')
	sys.stdout.flush()

def addValueToCsv(value, file):
	file.write(value + "\n")
	
def addValueToVector(value, vector):
	file.write(value + "\n")
	
accel = Accel()
accel.calibrate()

outFilename = "neoAcc" + strftime("%Y%m%d%H%M%S", gmtime()) + ".csv"
dataFile = open(directory + outFilename, "a")

print 'Output filename: ' + outFilename

values = list()

main(sys.argv[1:])

for i in range(0, cycles): # Run forever
	try:
		accelVals = accel.get() 
		modulus = math.sqrt((accelVals[0]*accelVals[0]) + (accelVals[1]*accelVals[1]) + (accelVals[2]*accelVals[2]))
		addValueToCsv(str(int(modulus)), dataFile)
		values.append(modulus)
		sleep(delay)
	except (KeyboardInterrupt, SystemExit):
		dataFile.flush()
		sys.exit()

plt.title(outFilename)
plt.plot(values)
plt.ylabel('acceleration magnitude')
plt.show()

dataFile.flush()
