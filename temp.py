# -*- coding: utf-8 -*-
"""
Created on Sat Jul 12 20:55:59 2014

@author: samthomas
"""

#imports
import numpy as np #for math
import matplotlib.pyplot as plt #for plotting
import Langmuir as lm

#data variables
data = lm.run(output=False) #get data using Langmuir
I = data[0] * -1 #current
V = data[1] #voltage

#size variables
fitReg = (2000, 3000) #fit region

def getTemp():
    i = np.log(I[fitReg[0]:fitReg[1]]) #take ln() of exponential region
    xVal = V[fitReg[0]:fitReg[1]] #voltage values for the fit region
    
    #find line coeficients
    lineCof = np.polyfit(xVal, i, 1)
    Te = 1/lineCof[0]
    
    print("Temp: " + str(Te))
    
    return Te, lineCof
    
def plot(plotExpFit = True, plotExpCurve = True):
    #choose number of subplots
    numSP = 0 #number of subplots
    if plotExpFit: numSP += 1
    if plotExpCurve: numSP += 1
    
    #setup subplots
    f, axarr = plt.subplots(numSP)
    
    #defining some variables    
    Te, lineCof = getTemp() #finding the Te  and line coeficients
    i = np.log(I[fitReg[0]:fitReg[1]]) #take ln() of exponential region
    xVal = V[fitReg[0]:fitReg[1]] #voltage values for the fit region
    lineVal = [lineCof[0] * x + lineCof[1] for x in xVal] #get values for the line
    expCurve = np.e**np.array(lineVal) #multiply line by e to get exponential curve
    
    #first subplot
    if (plotExpFit):
        if numSP == 1: _plotFindExpFit(axarr, xVal, i, lineVal)
        else:  _plotFindExpFit(axarr[0], xVal, i, lineVal)
    
    #second subplot    
    if (plotExpCurve):
        if numSP == 1: _plotExpCurve(axarr, xVal, expCurve)
        else: _plotExpCurve(axarr[1], xVal, expCurve)
    
    #show plot
    plt.xlabel("Voltage (v)")
    plt.ylabel("Current (I)")
    plt.show()
    
def _plotFindExpFit(axis, xVal, i, lineVal):
    axis.plot(xVal, i, "y")
    axis.plot(xVal, lineVal, "b--", linewidth = 2)
    axis.set_title("Finding Exponential Fit")
    axis.grid()
    
def _plotExpCurve(axis, xVal, expCurve):
    axis.plot(V, I, "y")
    axis.plot(xVal, expCurve, "b--", linewidth = 2)
    axis.set_title("Exponential Curve on Langmuir Data")
    axis.grid()
    
if __name__ == "__main__":
    plot(plotExpFit = False, plotExpCurve = True)
    
    
    
    