#Util file to make working with these files easier from the command line
import numpy as np
import matplotlib.pyplot as plt

#function to plot and show graphs
def plot(*args, **kwargs):
	eval(_makeEvalString(args))
	plt.show()

#TODO add key word args
def _makeEvalString(args):
	count = 0 #keep track of number of iterations
	evalString = 'plt.plot(' #string that will be evaluated
	
	#loop through all of the args
	for val in args:
		count += 1 #increment the count
		typ = type(val) #type of val
		
		#do different things based on type of arg
		if typ == type("String"):
			evalString += "'" + val + "'"
		elif typ == type(np.zeros(1)):
			val = val.tolist()
			evalString += _listToString(val)
		else:
			evalString += str(val)
			
		#if not the last arg add a comma else add a parenthese
		if count < len(args): evalString += ", "
		else: evalString += ")"
	
	return evalString
	
def _listToString(lst):
	string = "["
	count = 0
	for val in lst:
		count += 1
		string += str(val)
		
		#if not the last arg add a comma else add a bracket
		if count < len(lst): string += ", "
		else: string += "]"
		
	return string
	
	
	
	
	
	
	
	
	
	
	
