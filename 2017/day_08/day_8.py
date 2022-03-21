import re

with open("input.dat") as file:
    data = file.read().splitlines()
    

data = [re.split(' |, |\n',x) for x in data] 
registers= {}
maxvalue=0

for i in data:
    if i[0] not in registers:
     registers[i[0]]=0
    maxvalue=max(maxvalue,sorted(list(registers.values()))[-1])

    if i[3]=='if':
        if i[4] not in registers:
            registers[i[4]]=0
        if i[5]=='==':
            cond= registers[i[4]] == int(i[6])
        elif i[5]=='>=':
            cond= registers[i[4]] >= int(i[6])
        elif i[5]=='<=':
            cond= registers[i[4]] <= int(i[6])
        elif i[5]=='!=':
            cond= registers[i[4]] != int(i[6])
        elif i[5]=='>':
            cond= registers[i[4]] > int(i[6])
        elif i[5]=='<':
            cond= registers[i[4]] < int(i[6])
        else:
            print("Not clear what to do!")
    else:
        cond=True
    if cond:
        if i[1]=='inc':
            registers[i[0]]+=int(i[2])
        elif i[1]=='dec':
            registers[i[0]]-=int(i[2])

print(sorted(list(registers.values())))
print(maxvalue)

