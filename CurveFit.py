"""
Created on Wed Jul  9 22:07:57 2014

@author: samthomas
"""

#imports
import numpy as np
import Langmuir as lm

def makeArrayWithFit(fit, size):
    arr = np.arange(0, size, 1.0)
    count = 0
    for a in arr:
        arr[count] = (fit[0] * a**3) + (fit[1] * a**2) + (fit[2] * a) + fit[3]
        #print(a, arr[count])
        count += 1
        
    return arr
    
data = lm.run()
v = data[0] * -1
v = v[1800:2800]
cof = np.polyfit(np.arange(1000), v, 3)
fit = makeArrayWithFit(cof, 1000)