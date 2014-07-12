"""
Created on Wed Jul  9 22:07:57 2014

@author: samthomas
"""

#imports
import numpy as np
import Langmuir as lm
import matplotlib.pyplot as plt

#size vars
curveSize = (2000, 3000)
extLineNum = 1000
elSize = (2800, 3800) #ext line size
tlSize = (3800, 4800) #top line size

def makeArrayWithFit(fit, size):
    arr = np.arange(0, size, 1.0)
    count = 0
    for a in arr:
        arr[count] = (fit[0] * a**3) + (fit[1] * a**2) + (fit[2] * a) + fit[3]
        #print(a, arr[count])
        count += 1
        
    return arr
    
#each parameter is a tuple
def findIntersect(a1, a2, b1, b2):
    #variables
    eq1 = findCoef(a1, a2)
    eq2 = findCoef(b1, b2)
    c = eq1[0]
    Z = eq1[1]
    a = eq2[0]
    B = eq2[1]
    retX = ((B - Z) / (c - a))
    retY = c * retX + Z
    return (retX, retY)

def findCoef(a1, a2):
    #x1, y1, x2, y2, m, b = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    x1, y1 = float(a1[0]), float(a1[1])
    x2, y2 = float(a2[0]), float(a2[1])
    #print(x1, y1, x2, y2, type(x1))
    m = ((y2 - y1) / (x2 - x1))
    b = ((m * x1) - y1) * -1
    #print("fc", x1, y1, x2, y2, m, b)
    return (m, b)
    
def run():
    
    #data    
    data = lm.run()
    v = data[0] * -1
    
    #first curve fit
    vRef = v[curveSize[0]:curveSize[1]]
    curveCof = np.polyfit(np.arange(len(vRef)), vRef, 3)
    curveFit = makeArrayWithFit(curveCof, len(vRef))
    
    #extended curve in line
    points = curveFit[len(vRef) - 2:len(vRef)] #take last two points of fit
    lineCof = np.polyfit(np.arange(2), points, 1)
    extlineFit = [lineCof[0] * c + lineCof[1] for c in np.arange(extLineNum)]
    
    #line fit the top portion
    size = (tlSize[0], tlSize[1])
    top = v[size[0]:size[1]]
    topCof = np.polyfit(np.arange(size[0],size[1]), top, 1)
    topLineFit = [topCof[0] * c + topCof[1] for c in np.arange(size[0] - 1000,size[1])]
    
    #plotting
    plt.plot(v, "y", label = "Test", linewidth = 1) #main curve
    plt.plot(np.arange(curveSize[0], curveSize[1]), curveFit, "b", linewidth = 2) #fitted curve 3rd degree
    plt.plot(np.arange(elSize[0], elSize[1]), extlineFit, "b--", linewidth = 2) #fitted line
    plt.plot(np.arange(size[0] - 1000, size[1]), topLineFit, "r", linewidth = 2)
    
    #intersection
    a1, a2 = (elSize[0], extlineFit[0]), (elSize[1], extlineFit[999])
    b1, b2 = (size[0] - 1000, topLineFit[0]), (size[1], topLineFit[1999])
    inter = findIntersect(a1, a2, b1, b2)
    print("inter", inter)
    plt.plot(inter[0], inter[1], "ko")
    
    #showing plot
    plt.xlabel("Index")
    plt.ylabel("Current")
    plt.title("Intersection: (" + str(inter[0]) + ", " + str(inter[1]) + ")")
    #plt.xlim(3425, 3426)
    #plt.ylim(0.04646, 0.04660)
    plt.grid()
    plt.show()

def graphLog():
    data = lm.run()
    I = data[0] * -1
    v = data[1]
    i = I[curveSize[0]:curveSize[1]]
    i = np.log(i)
    plt.plot(v[0:1000], i)
    lineCof = np.polyfit(v[curveSize[0]:curveSize[1]], i, 1)
    print(lineCof)
    line = [lineCof[0] * x + lineCof[1] for x in np.arange(1000)]
    plt.plot(v[0:1000], line)
    #line = np.e**np.array(line)
    #line *= 0.01
    #plt.plot(v[curveSize[0]:curveSize[1]], line, "b--", linewidth=2)
    #plt.plot(v, I, "y")
    #plt.title("Eq: " + str(lineCof[0]) + "x + " + str(lineCof[1]))

    ret = []
    for v in v[curveSize[0]:curveSize[1]]:
        ret.append((-v) / lineCof[0])

    print("Te: " + str(1/lineCof[0]))
    plt.grid()
    #plt.show()

if __name__ == "__main__":
    graphLog()
