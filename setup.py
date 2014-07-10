#imports
import sys
import os

files = ["Langmuir.py", "ReadCSV.py", "UtilPlot.py"]

if __name__ == "__main__":
	fileDir = os.path.dirname(os.path.realpath(__file__)) #gets current dir
	fileDir += "/"
	for s in files:
		print(s + " added to path")
		sys.path.append(fileDir + s)
