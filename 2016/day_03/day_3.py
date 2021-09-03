import re

with open("input.dat") as file:
    data = file.readlines()
    
data = [re.split('\n|\s+',x) for x in data]

counter=0

for i in data:
    l=sorted([int(j) for j in i[1:4]])
    if l[0]+l[1]>l[2]:
        counter+=1
        
print(counter)

counter=0
        
for i in range(len(data)):
    if i%3==0:
        for j in range(1,4):
            l=sorted([int(data[i][j]),int(data[i+1][j]),int(data[i+2][j])])
            if l[0]+l[1]>l[2]:
                counter+=1
        
print(counter)
