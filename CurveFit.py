"""
Created on Wed Jul  9 22:07:57 2014

@author: samthomas
"""

#imports
import numpy as np
import Langmuir as lm
import matplotlib.pyplot as plt

def makeArrayWithFit(fit, size):
    arr = np.arange(0, size, 1.0)
    count = 0
    for a in arr:
        arr[count] = (fit[0] * a**3) + (fit[1] * a**2) + (fit[2] * a) + fit[3]
        #print(a, arr[count])
        count += 1
        
    return arr

#data    
data = lm.run()
v = data[0] * -1

#first curve fit
vRef = v[1800:2800]
curveCof = np.polyfit(np.arange(1000), vRef, 3)
curveFit = makeArrayWithFit(curveCof, 1000)

#extended curve in line
points = curveFit[998:1000] #take last two points of fit
lineCof = np.polyfit(np.arange(2), points, 1)
extlineFit = [lineCof[0] * c + lineCof[1] for c in np.arange(1000)]

#line fit the top portion
size = (3800, 4800)
top = v[size[0]:size[1]]
topCof = np.polyfit(np.arange(size[0],size[1]), top, 1)
topLineFit = [topCof[0] * c + topCof[1] for c in np.arange(size[0] - 1000,size[1])]

#plotting
plt.plot(v, "y", label = "Test", linewidth = 1) #main curve
plt.plot(np.arange(1800, 2800), curveFit, "b", linewidth = 2) #fitted curve 3rd degree
plt.plot(np.arange(2800, 3800), extlineFit, "b--", linewidth = 2) #fitted line
plt.plot(np.arange(size[0] - 1000, size[1]), topLineFit, "r", linewidth = 2)

#showing plot
plt.xlabel("Index")
plt.ylabel("Current")
plt.show()







