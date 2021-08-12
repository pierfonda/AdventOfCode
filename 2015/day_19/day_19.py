#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 12:28:57 2021

@author: pier
"""
from collections import defaultdict

with open("input.dat") as file:
    data = file.readlines()
    
data_dict = defaultdict(list)
dict_data={}
molecule=data[-1].strip("\n")

for i in data:
    if i.strip("\n")=='':
        break
    i=i.strip("\n").split(" => ")
    data_dict[i[0]].append(i[1])

data_dict=dict(data_dict)

for v in data_dict:
    for j in data_dict[v]:
        dict_data[j]=v

n_rep=0
list_replacements=[]

for j in range(len(molecule)):
    if molecule[j] in data_dict:
        n_rep+=len(data_dict[molecule[j]])
        for k in data_dict[molecule[j]]:
            list_replacements.append(molecule[:j]+k+molecule[j+1:])
    if j< len(molecule)-1:
        if  molecule[j]+molecule[j+1] in data_dict:
            n_rep+=len(data_dict[molecule[j]+molecule[j+1]])
            for k in data_dict[molecule[j]+molecule[j+1]]:
                list_replacements.append(molecule[:j]+k+molecule[j+2:])
        
print(len(set(list_replacements)))

initial_string="e"

def extend_string(string):
    out_string=[]
    if isinstance(string,str):
        for j in range(len(string)):
            if string[j] in data_dict:
                for k in data_dict[string[j]]:
                    out_string.append(string[:j]+k+string[j+1:])
            if j< len(string)-1:
                if  string[j]+string[j+1] in data_dict:
                    for k in data_dict[string[j]+string[j+1]]:
                        out_string.append(string[:j]+k+string[j+2:])
        return out_string
    else:
        for l in string:
            out_string.append(extend_string(l))
        return [x for y in out_string for x in y]

#t_str=initial_string
#for i in range(2):
#    t_str=extend_string(t_str)
#    print(len(t_str))
        
def string_replace_pos(string, substring, replacement, pos):
    find = string.find(substring)
    i = find != -1
    while find != -1 and i != pos:
        find = string.find(substring, find + 1)
        i += 1
    if i == pos:
        return string[:find] + replacement + string[find+len(substring):]
    return string
        
def compact_string(string):
    max_length=1000
    if string==None:
        return None
    out_string=[]
    if isinstance(string,str):
        for i in dict_data:
            if i in string:
                for j in range(string.count(i)):
                    out_string.append(string_replace_pos(string,i,dict_data[i],j+1))
        out_string = list( dict.fromkeys(out_string) )
        if len(out_string)>max_length:
            return sorted(out_string,key=len)[:max_length]
        if len(out_string)>0:
            return sorted(out_string,key=len)
        else:
            return None
    else:
        for l in string:
            out_string.append(compact_string(l))
        if out_string==[None]:
            return None
        out_string=[x for y in out_string for x in y]
        out_string = list( dict.fromkeys(out_string) )
        if len(out_string)>max_length:
            return sorted(out_string,key=len)[:max_length]
        if len(out_string)>0:
            return sorted(out_string,key=len)
        else:
            return None
    
t_str=molecule
i=0
while t_str!=None and i<1000:
    print(i,len(t_str),set([len(x) for x in t_str]),[x for x in t_str if len(x)<10])
    i+=1
    t_str=compact_string(t_str)