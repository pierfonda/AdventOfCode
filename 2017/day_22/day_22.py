#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:50:45 2022

@author: pier
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


with open("input.dat") as file:
    data = file.read().splitlines()
    data = np.array([[i for i in j]for j in data],dtype=str)

ly,lx=data.shape
infected=[]
    
for i in range(ly):
    for j in range(lx):
        if data[i,j]=='#':
            infected.append([j-lx//2,ly//2-i])

start=[[0,0],[0,1]] 
pos=start    
# print(infected)

n=0
for _ in range(10000):
    if pos[0] in infected:
        infected.remove(pos[0])
        pos[1]=[pos[1][1],-pos[1][0]]
        pos[0]=[a+b for a,b in zip(pos[0],pos[1])]
        # print(f"It is infected!\t\t Now in {pos[0]} and {len(infected)}")
    else:
        infected.append(pos[0])
        pos[1]=[-pos[1][1],pos[1][0]]  
        pos[0]=[a+b for a,b in zip(pos[0],pos[1])]
        n+=1
        # print(f"It is not infected!\t Now in {pos[0]} and {len(infected)}")

print(n)   

status=defaultdict(lambda:0)
nsteps=10000000

def gpos(p,ns):
    return 2*p[0]*ns+p[1]
    
for i in range(ly):
    for j in range(lx):
        if data[i,j]=='#':
            status[gpos([j-lx//2,ly//2-i],nsteps)]=2
            # infected.append([j-lx//2,ly//2-i])
            
start=[[0,0],[0,1]] 
pos=start    

n=0
for i in range(nsteps):
    """ 
    Statuses:
        Clean:0
        Weakened:1
        Infected:2
        Flagged:3   
    Rules:
        1 -> 2 (W->I)
        2 -> 3 (I->F)
        3 -> 0 (F->C)
        0 -> 1 (C->W)
        """
    pkey=gpos(pos[0],nsteps)
    psta=status[pkey]
    if psta==1:
        status[pkey]=2
        pos[0]=[a+b for a,b in zip(pos[0],pos[1])]
        n+=1
        # print(f"It is weakened!\t\t Now in {pos[0]} and {psta}")
    elif psta==2:
        status[pkey]=3
        pos[1]=[pos[1][1],-pos[1][0]]
        pos[0]=[a+b for a,b in zip(pos[0],pos[1])]
        # print(f"It is infected!\t\t Now in {pos[0]} and {psta}")
    elif psta==3:
        status[pkey]=0
        pos[1]=[-pos[1][0],-pos[1][1]]
        pos[0]=[a+b for a,b in zip(pos[0],pos[1])]
        # print(f"It is flagged!\t\t Now in {pos[0]} and {psta}")
    else:
        status[pkey]=1
        pos[1]=[-pos[1][1],pos[1][0]]  
        pos[0]=[a+b for a,b in zip(pos[0],pos[1])]
        # print(f"It is clean!\t\t Now in {pos[0]} and {psta}")
    

print(n)
