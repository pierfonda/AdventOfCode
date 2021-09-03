#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 12:02:49 2021

@author: pier
"""

with open("input.dat") as file:
    #data = file.read()
    content= file.readlines()
    
content = [x.strip() for x in content] 

atot=0
ribbon=0
    
for x in content:
    y=[int(y) for y in x.split("x")]
    y=sorted(y)
    atot+=3*y[0]*y[1]+2*y[1]*y[2]+2*y[0]*y[2]
    ribbon+=2*(y[0]+y[1])+y[0]*y[1]*y[2]

print(atot)
print(ribbon)