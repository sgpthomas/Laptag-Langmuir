def read_csv(filepath, output = False):
    #variables
    header = []
    returnArr = []
    state = True
    
    #open file in read mode
    readFile = open(filepath, 'r')
    
    #raw data from file split by lines
    rawData = readFile.read().split("\r\n")
    
    #main for loop that loops through all of the lines
    for line in rawData:
        #check if line is part of header
        if line.find('"') != -1:
            header.append(line)
        #else line is not part of header
        else:
            #Make array if haven't already
            if state:
                #this makes an array of the right dimensions for the csv
                for n in line.split(','):
                    returnArr.append([])
                state = False
                
            val = line.split(',') #splits the line into individual values
            #loops through each value in val
            index = 0 #keep track of where we are
            for v in val:
                try: v = float(v)
                except: v = v
                returnArr[index].append(v) #append value to correct place
                index += 1
        
      #print header
    #print("Header", header)
    if output: print("Reading File:" + filepath)
        
    #close file
    readFile.close()
    
    #return something
    return returnArr

#statement to make sure that this file is not run by itself
if __name__ == "__main__":
    read_csv("data/C1_LP_heatpulse_00000.txt")
