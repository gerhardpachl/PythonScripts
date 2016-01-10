# -*- coding: utf-8 -*-
"""
Introduction to Python
Python Exrecise / Training based on example of Jason Briggs snake wrangling for kids
This is a temporary script file.
"""
# python tst program -*- coding: utf-8 -*
# create a random number
# user has to find out these numbers by choosing a number in a given range 

import random

num = random.randint(1,10)

while True:
    print "choose a number between 1 an 10"
    value = raw_input()
    i = int(value)

    if i == num:
        print "You are right"
        break

    elif i < num:
        print "try a higher number"

    elif i > num:
        print "try a lower number"
