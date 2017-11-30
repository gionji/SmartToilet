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
directory = "data/"
outFilename = ""
delay = 0.05

windowSize = 20
magnitudeTh = 300
eventTh = 10
########################

def main(argv):
	global delay
	global cycles
	try:
		opts, args = getopt.getopt(argv,"d:t:w:m:")
	except getopt.GetoptError:
		print 'test.py -d <delay_seconds>  -w <sliding win size> -m magnitudeTh -t eventTH'
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-d"):
			delay = float(arg)
		elif opt in ("-m"):
			magnitudeTh = int(arg)
		elif opt in ("-w"):
			windowSize = int(arg)
		elif opt in ("-t"):
			eventTh = int(arg)


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
window = list()

main(sys.argv[1:])

while True: # Run forever
	try:
		accelVals = accel.get() 
		modulus = math.sqrt((accelVals[0]*accelVals[0]) + (accelVals[1]*accelVals[1]) + (accelVals[2]*accelVals[2]))
		
		updateWindow(modulus)
		
		if getMovementIndex(window) > eventTh:
			eventStatus = 1
		else:
			eventStatus = 0
		
		if eventStatus != prevEventStatus:
			statusChange()
		
		prevEventStatus = eventStatus
			
		sleep(delay)
	except (KeyboardInterrupt, SystemExit):
		sys.exit()
