#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import floor
import json

with open("input.dat") as file:
    data = file.readlines()
data = [x.strip() for x in data]

#print(*data,sep="\n")

valuelist=[]

for i in data:
    j=i.split(" ")
    valuelist.append([j[0],int(j[3]),int(j[6]),int(j[-2])])
    
#print(*valuelist,sep="\n") 
    
def travel(rlist,seconds):    
    traveled= rlist[1]*rlist[2]*(floor(seconds/(rlist[2]+rlist[3]))) + rlist[1]*min(rlist[2],(seconds % (rlist[2]+rlist[3])))
    return traveled

travelresult=[]
finalseconds=2503

for i in valuelist:
    travelresult.append([i[0],travel(i,finalseconds)])

travelresult.sort(key= lambda x: x[1],reverse=True)

print(*travelresult,sep="\n")

scorelist={}

for i in valuelist:
    scorelist[i[0]]=0    

for j in range(finalseconds):
    travelresult=[]
    for i in valuelist:
        travelresult.append([i[0],travel(i,j+1)])
    travelresult.sort(key= lambda x: x[1],reverse=True)
    for k in travelresult:
        if k[1]==travelresult[0][1]:
            scorelist[k[0]]+=1
            
print(json.dumps(scorelist, indent = 4))