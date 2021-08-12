#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 18:12:35 2021

@author: pier
"""

with open("input.dat") as file:
    data = file.readlines()
data = [x.strip() for x in data]   

rawlength=0
codelength=0
htgneledoc=0
for i in data: 
    codelen=0
    neledoc=len(i)
    j=0
    while j<len(i):
        if i[j]=="\"":
            j+=1
            neledoc+=1
        elif i[j]=="\\":
            neledoc+=1
            if i[j+1]=="x":
                codelen+=1
                j+=4
            elif i[j+1]=="\"":
                codelen+=1
                neledoc+=1
                j+=2
            elif i[j+1]=="\\":
                codelen+=1
                neledoc+=1                
                j+=2
            else:
                codelen+=1
                j+=2
        else:
            codelen+=1
            j+=1
    neledoc+=2
#    print(len(i),codelen,neledoc)
    rawlength+=len(i)   
    codelength+=codelen
    htgneledoc+=neledoc

    
print("Total length",rawlength,"\nCode length",codelength,"\nDifference",rawlength-codelength,"\nEncoded length",htgneledoc,"\nDifference",htgneledoc-rawlength)
