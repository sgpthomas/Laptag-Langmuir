#imports
import UtilPlot as up
import Langmuir as lm
import numpy as np

def main():
    #loop through all the files
    data = lm.run()
    i = data[1]
    v = data[0]
    v *= -1
    v = v[1800:2800]
    up.plot(np.arange(1000), v, "k")
    fit = np.polyfit(np.arange(1000), v, 3)
    fit = makeArrayWithFit(fit, 1000)
    up.plot(np.arange(1000), fit, "b")
    
def makeArrayWithFit(fit, size):
    arr = np.arange(size)
    count = 0
    for a in arr:
        arr[count] = (fit[0] * a**3) + (fit[1] * a**2) + (fit[2] * a) + fit[3]
        count += 1
        
    return arr

if __name__ == "__main__":
    main()
