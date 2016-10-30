#!/usr/bin/python

import sys, json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import urllib2

time = []
moistureReadings = []

#dataDir = "/home/cvilela/Arduino/PlantSitter/Data/"

stream = "roaGpWRoAwI692ZnG9gA"

# https://data.sparkfun.com/output/roaGpWRoAwI692ZnG9gA.json
def main ():


    dataStream = urllib2.urlopen('https://data.sparkfun.com/output/'+stream+'.json')

 #   print dataStream
    jsonData = dataStream.read()
 #   print jsonData
    data = jsonData[0]
 
#    data = json.load(dataStream)

    
#    print data[0]
    
    index = 0
    for entry in data :
        print entry
        print entry["timestamp"], entry["moisture"]
        time.append(index)
        index += 1
        moistureReadings.append(float(entry["moisture"]))
        
        # 2016-10-10T02:24:00.639Z
        #            time.append(datetime.strptime(entry["timestamp"], "%Y-%m-%dT%H:%M:%SZ"))
        #            time.append(datetime.fromtimestamp(entry["timestamp"]))
        #            time.append(entry["timestamp"])
    
         
    moistureSmooth = movingaverage(moistureReadings, 500)
    plt.plot(time,moistureSmooth)
    plt.show()

    raw_input()
        

def movingaverage(interval, window_size):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')
        

if __name__ == "__main__" :
    main()
