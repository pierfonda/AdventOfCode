#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

with open("input.dat") as file:
    data = file.readlines()
data = [x.strip() for x in data]   

# Check if command is suitable for assignment
def check_command(vec):
    flag=0
#   print(vec)
    for ve in vec:
        if not(str(ve).isdigit()) and ve!="NOT" and ve!="AND" and ve!="OR" and ve!="LSHIFT" and ve!="RSHIFT":
            flag=1
    if flag==0:
        return True
    else:
        return False
    
def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

# Reset variables
for i in range(len(data)):
        v=list(filter(None,re.split("->| ",data[i])))
        exec("variable_%s = None" % v[-1])



# Main loop
counter=0
safe_counter=0
variable_b=46065
counter+=1
while counter<len(data) and safe_counter<1000000:
    for i in range(len(data)):
        v=list(filter(None,re.split("->| ",data[i])))
        for j in range(len(v)):
            if v[j].isdigit():
                v[j]=int(v[j])
            else:
                if eval('variable_'+v[j]) is not None:
                    v[j]=int(eval('variable_'+str(v[j])))
        if check_command(v[:-1]) and not(is_digit(v[-1])):
            if "NOT" in v:
                if eval('variable_'+v[-1])==None:
                    counter+=1            
                exec("variable_%s = %s" % (v[-1],~v[1] & 0xffff))
                print("Assigned to",'variable_'+v[-1],"the value",eval('variable_'+v[-1]))         
            elif "AND" in v:
                if eval('variable_'+v[-1])==None:
                    counter+=1                   
                exec("variable_%s = %s" % (v[-1],v[0]&v[2]))
                print("Assigned to",'variable_'+v[-1],"the value",eval('variable_'+v[-1]))             
            elif "OR" in v:
                if eval('variable_'+v[-1])==None:
                    counter+=1                   
                exec("variable_%s = %s" % (v[-1],v[0]|v[2]))
                print("Assigned to",'variable_'+v[-1],"the value",eval('variable_'+v[-1]))        
            elif "LSHIFT" in v:
                if eval('variable_'+v[-1])==None:
                    counter+=1                   
                exec("variable_%s = %s" % (v[-1],v[0]<<v[2]))
                print("Assigned to",'variable_'+v[-1],"the value",eval('variable_'+v[-1]))
            elif "RSHIFT" in v:
                if eval('variable_'+v[-1])==None:
                    counter+=1   
                exec("variable_%s = %s" % (v[-1],v[0]>>v[2]))
                print("Assigned to",'variable_'+v[-1],"the value",eval('variable_'+v[-1]))
            else:
                if eval('variable_'+v[-1])==None:
                    counter+=1                 
                exec("variable_%s = %s" % (v[1],v[0]))
                print("Assigned to",'variable_'+v[1],"the value",eval('variable_'+v[1]))
        safe_counter+=1

print(variable_a,safe_counter)