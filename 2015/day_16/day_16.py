import re

with open("input.dat") as file:
    data = file.readlines()
data = [x.strip() for x in data]

with open("aunt.dat") as file:
    aunt = file.readlines()
aunt = [x.strip() for x in aunt]

dictaunt = dict()
for i in range(len(aunt)):
    j=re.split(': |, | ',aunt[i])
    dictaunt[j[0]]=int(j[1])

dictlist = [dict() for x in range(len(data))]

for i in range(len(data)):
    j=re.split(': |, | ',data[i])
    for k in range(len(j)-1):
        if not k % 2:
            dictlist[i][j[k]]=int(j[k+1])

sue= [True for x in range(len(dictlist))]

dplus=['cats','trees']
dminus=['pomeranians','goldfish']
    
for i in range(len(dictlist)):
    for j in dictaunt:
        if j in dictlist[i] and j not in dplus and j not in dminus and dictaunt[j]!=dictlist[i][j]:
            sue[i]=False
        if j in dictlist[i] and j in dplus and dictaunt[j]>=dictlist[i][j]:
            sue[i]=False
        if j in dictlist[i] and j in dminus and dictaunt[j]<=dictlist[i][j]:
            sue[i]=False
            
for i in range(len(dictlist)):
    if sue[i]:
        print("The true Sue is:",dictlist[i]['Sue'])