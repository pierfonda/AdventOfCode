#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:22:57 2021

@author: pier
"""
import math 
import matplotlib.pyplot as plt
import numpy as np
import time

def one_step(grid_in, edges=False):
    xd,yd = grid_in.shape
    grid_out=np.copy(grid_in)
    for i in range(xd):
        for j in range(xd):
            n=0
            for xi in range(1,-2,-1):
                for xj in range(1,-2,-1):
                    if i+xi>=0 and j+xj>=0 and i+xi<xd and j+xj<yd and (xi|xj)!=0:
                        if grid_in[j+xj][i+xi]==1:
                            n+=1
            if grid_in[j][i]==1 and n!=3 and n!=2:
                grid_out[j][i]=0
            elif grid_in[j][i]==0 and n==3:
                grid_out[j][i]=1
    if edges:
        grid_out[0][0]=1
        grid_out[0][-1]=1
        grid_out[-1][-1]=1
        grid_out[-1][0]=1
    grid_in=grid_out
    grid_out=None
    return grid_in

def count_lights(grid_in):
    xd,yd = grid_in.shape
    n=0
    for i in range(xd):
        for j in range(xd):
            if grid_in[j][i]==1:
                n+=1
    return n
         
with open("input.dat") as file:
    data = file.read()

data=data.replace("\n", "")
xlen,ylen= int(math.sqrt(len(data))),int(math.sqrt(len(data)))

#Initialize grid from data
grid = np.zeros((xlen,ylen),dtype=int)
for i in range(xlen):
    for j in range(ylen):
        if data[i+j*xlen]=='#':
            grid[j][i]=1
            
grid[0][0]=1
grid[0][-1]=1
grid[-1][-1]=1
grid[-1][0]=1

time_series=[]
for i in range(101):
    plt.imshow(grid, cmap='Greys',  interpolation='nearest')
    plt.title(str(count_lights(grid))+" lights are on at step "+str(i))
    plt.show()
    time.sleep(.01)
    time_series.append([i,count_lights(grid)])
    grid=one_step(grid,True)
    
x, y = zip(*time_series)
plt.plot(x,y)
