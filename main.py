#imports
import UtilPlot as up
import Langmuir as lm

def main():
	#loop through all the files
	data = lm.analyzeData()
	i = data[1]
	v = data[0]
	up.plot(i, -v, "k")
	
if __name__ == "__main__":
	main()
