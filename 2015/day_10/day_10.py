#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 12:48:07 2021

@author: pier
"""

def lookandsay(string):
    string=string+" "
    counter=1
    outstr=""
    for i in range(len(string)-1):
        if string[i+1]==string[i]:
            counter+=1           
        else:
#           print(counter,string[i],i)
            outstr+=str(counter)+string[i]
            counter=1
    return outstr
        
initstring="1113122113"

for i in range(50):
    initstring=lookandsay(initstring)
    
print(len(initstring))