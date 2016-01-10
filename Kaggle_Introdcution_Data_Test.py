# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 16:47:25 2016
Introduction Python & Kaggle Titanic case
Exploring NumPy: based on example of Getting Started with Python: Kaggle's Titanic Competition

"""
Getting Started with Python: Kaggle's Titanic Competition

import csv as csv 
import numpy as np

# Open up the csv file in to a Python Numpy array object
ar_Ship_Passg = csv.reader(open('../My_Pythons/CSV/train.csv', 'rb')) 
header = ar_Ship_Passg.next()  # The next() command just skips the 
                                 # first line which is a header
data=[]                          # Create a variable called 'data'.
for row in ar_Ship_Passg:        # Run through each row in the csv file,
    data.append(row)             # adding each row to the data variable
data = np.array(data) 	         # Then convert from a list to an array
			                        # Be aware that each item is currently
                                 # a string in this format
print (data) 














