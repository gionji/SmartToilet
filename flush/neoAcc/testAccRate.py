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
	
#########################
delay = 0.05
########################

def main(argv):
	global delay
	try:
		opts, args = getopt.getopt(argv,"d:")
	except getopt.GetoptError:
		print 'test.py -d <delay_seconds> '
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-d"):
			delay = float(arg)


def dot():
	sys.stdout.write('.')
	sys.stdout.flush()

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

def statusChange():
	global eventStatus
	print str(eventStatus)

accel = Accel()
accel.calibrate()

values = list()

main(sys.argv[1:])

for i in range(0, 50): # Run forever
	try:
		accelVals = accel.get() 
		modulus = math.sqrt((accelVals[0]*accelVals[0]) + (accelVals[1]*accelVals[1]) + (accelVals[2]*accelVals[2]))
		values.append(modulus)			
		sleep(delay)
	except (KeyboardInterrupt, SystemExit):
		sys.exit()

for v in values:
	print str(v)