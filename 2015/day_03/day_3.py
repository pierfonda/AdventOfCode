#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:27:52 2021

@author: pier
"""
pos=[0,0]
posS=[0,0]
posR=[0,0]
houselist=[]
houselist2=[]
RorS=True


with open("input.dat") as file:
    data = list(file.read())

for i in data:
    if i=='>':
        pos[0]+=1
        if RorS : 
            posS[0]+=1 
        else : 
            posR[0]+=1
    elif i=='<':
        pos[0]-=1
        if RorS : 
            posS[0]-=1 
        else : 
            posR[0]-=1    
    elif i=='^':
        pos[1]+=1
        if RorS : 
            posS[1]+=1 
        else : 
            posR[1]+=1
    elif i=='v':
        pos[1]-=1
        if RorS : 
            posS[1]-=1 
        else : 
            posR[1]-=1
    if pos not in houselist:
        houselist=houselist+[[pos[0],pos[1]]]
    if posR not in houselist2:
        houselist2=houselist2+[[posR[0],posR[1]]]
    if posS not in houselist2:
        houselist2=houselist2+[[posS[0],posS[1]]]
    RorS=not(RorS)

print(len(houselist))
print(len(houselist2))