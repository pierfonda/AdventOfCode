#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:23:59 2021

@author: pier
"""

def check_vowels(str):
  return str.count('a')+str.count('e')+str.count('i')+str.count('o')+str.count('u')

def check_doubles(str):
  for i in range(len(str)-1):
      if str[i+1]==str[i]:
          return True
          break
      
def check_pairs(str):
  return str.count('ab')+str.count('cd')+str.count('pq')+str.count('xy')

def check_fourples(str):
  for i in range(len(str)-3):
      for j in range(i+2,len(str)-1):
          if str[i]==str[j] and str[i+1]==str[j+1]:
 #             print(str,str[i]+str[i+1])
              return True
              break
          
def check_triples(str):
  for i in range(len(str)-2):
      if str[i]==str[i+2]:
 #         print(str,str[i]+str[i+1]+str[i+2])
          return True
          break

with open("input.dat") as file:
    data = file.readlines()

data = [x.strip() for x in data]

nice=0 

for i in data:
    if check_vowels(i)>=3 and check_doubles(i) and check_pairs(i)==0:
        nice+=1
#        print(i)
#    if nice>10:
#        break
         
    
print("First criterion: ",nice)

nice=0

for i in data:
    if check_triples(i) and check_fourples(i):
        nice+=1
print("Second criterion: ",nice)