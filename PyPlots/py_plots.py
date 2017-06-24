# -*- coding: utf-8 -*-
"""
Karim Oumghar
Css 455
Files, Masks, and Plotting

It took a while to figure out how to handle bad data
and to figure out where the bad data was
also I took some time to learn masked arrays better
What I tried to do was only use data that was good
so lines that had missing fields were not included 
in the temperatures or julian days

Anyways, I think the results were good, at the very least
"""

# -*- coding: utf-8 -*-
import os
import sys
import numpy.ma as n
import matplotlib.pyplot as plt

#I had a couple of errors that brought up encoding stuff
#when I tried reading in data, this is a fix
reload(sys)
sys.setdefaultencoding('utf8')
#file i/o stuff, declare the path of both data file and output picture
myFilePath = os.path.join(os.getcwd(), 'Documents', 'ASFG_Ts.txt')
myOutputPath = os.path.join(os.getcwd(), 'Documents',\
'oumghar, karim-py_files_plots.png')
dataFile = open(myFilePath)

#read in all lines
listOfData = dataFile.readlines()

#------------this block for testing purposes only...-----------------
line = listOfData[1504]
list_ = []
temp = line.split('\t')
data = n.masked_array(temp)
list_.append(data[0])
print temp[0], len(temp)
#--------------------------------------------------------------------

#two lists, temperatures, julian days
temperatures = []
julian_days = []

#start our loop at index 3, since the data starts there
for i in range(3, len(listOfData)):
    #split each line
    #store each piece of data in its own list

    line = listOfData[i]
    split_data = line.split('\t')
    temp_maskedarr = n.masked_array(split_data)
    
    #assume the data we add is only good
    if '\n' not in temp_maskedarr and len(temp_maskedarr) > 3:
        try:
            julian_days.append(temp_maskedarr[0])
            temperatures.append(temp_maskedarr[3])
        except IndexError:
            continue


#convert the lists into masked arrays of type float
temps = n.masked_array(temperatures, dtype=float)
dates = n.masked_array(julian_days, dtype=float)
plt.xlabel('Julian Days')
plt.ylabel('Temperature (°C)')
plt.title('SHEBA Experiment')
plt.xlim([300,650])
plt.ylim([-60,10])
plt.plot(julian_days, temps, 'b')
plt.savefig(myOutputPath)
plt.show()
"""doc string"""
