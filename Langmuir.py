#imports
import ReadCSV as csv
import numpy as np

#parameters
dataDir = "data/"
currentCh = "C1"
voltageCh = "C3"
baseFileName = "_LP_heatpulse_000"
fileExt = ".txt"

#choose file name based on index
def chooseFileName(index, channel):
	if index < 10:
		return dataDir + channel + baseFileName + "0" + str(index) + fileExt
	else:
		return dataDir + channel + baseFileName + str(index) + fileExt
		
def analyzeData():
	#variables
	count = 0
	currentSum = np.zeros([4800])
	voltageSum = np.zeros([4800])
	#loop through all the files and get the relevant data
	for i in range(24):
		current = csv.read_csv(chooseFileName(i, currentCh))
		current = current[4]
		current = current[2200:7000]
		voltage = csv.read_csv(chooseFileName(i, voltageCh))
		voltage = voltage[4]
		voltage = voltage[2200:7000]
		
		currentSum += current
		voltageSum += voltage
		count += 1
		
	#divide by count to get average
	currentSum /= count
	voltageSum /= count
	
	#return
	return [currentSum, voltageSum]
