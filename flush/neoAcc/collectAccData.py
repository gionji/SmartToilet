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

prevEventStatus = 0
eventStatus = 0
enabledAxis = ''
	
directory = 'data/'

#########################
delay = 0.05
filename = ''
########################

def main(argv):
	global filename, delay
	try:
		opts, args = getopt.getopt(argv,"f:d:")
	except getopt.GetoptError:
		print 'test.py -f <filename> -d <delay>'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-f"):
			filename = str(arg)
		if opt in ("-d"):
			delay = float(arg)

	# open accelerometer
	accel = Accel()
	#accel.calibrate()

	values = list()

	while True: # Run forever
		try:
			accelVals = accel.get() 
			modulus = math.sqrt((accelVals[0]*accelVals[0]) + (accelVals[1]*accelVals[1]) + (accelVals[2]*accelVals[2]))
			values.append( str(accelVals[0]) + ','+ str(accelVals[1]) + ','+ str(accelVals[2]) + ','+ str(modulus) )			
			sleep(delay)
		except (KeyboardInterrupt, SystemExit):
			writeToCsv(values, str(filename))
			sys.exit()


def dot():
	sys.stdout.write('.')
	sys.stdout.flush()

def addValueToCsv(value, file):
	file.write(value + "\n")

def statusChange():
	global eventStatus
	print str(eventStatus)

def writeToCsv(values, name):
	global delay
	outFilename = "neoAcc_" + str(name) + '_' +str(int(delay*1000))+ "ms.csv"
	dataFile = open(directory + outFilename, "a")

	dataFile.write('===============================\n')

	for v in values:
		dataFile.write(v+'\n')
	
	dataFile.flush()
	dataFile.close()



if __name__ == "__main__":
	main(sys.argv[1:])
