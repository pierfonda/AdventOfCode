#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 12:28:57 2021

@author: pier
"""
import sys
from sympy.ntheory import divisors

top_int=sys.maxsize
max_value=34000000
list_presents=[]
list_presents_new=[]

for i in range(1,top_int):
    divs=divisors(i)
    sum_divs_new=0
    list_presents.append(10*sum(divs))
    for j in divs:
        if i/j<50:
            sum_divs_new+=11*j
    list_presents_new.append(sum_divs_new)
#    print(list_presents[-1])
#   if list_presents[-1]>max_value:
    if list_presents_new[-1]>max_value:
        print("Found",i,"with value",list_presents_new[-1],"which is bigger than",max_value)
        break

