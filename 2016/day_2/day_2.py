import re

with open("input.dat") as file:
    data = file.readlines()
    
data = [re.split('\n',x) for x in data]

dicpart1={
        (1,1):3,
        (1,0):6,
        (1,-1):9,
        (0,1):2,
        (0,0):5,
        (0,-1):8,
        (-1,1):1,
        (-1,0):4,
        (-1,-1):7,
        }

print("First part:")


for i in data:
    initialpoint=[0,0]
    for j in i[0]:
        if j=='U' and initialpoint[1]<1:
            initialpoint[1]+=1          
        elif j=='D' and initialpoint[1]>-1:
            initialpoint[1]-=1          
        elif j=='R' and initialpoint[0]<1:
            initialpoint[0]+=1
        elif j=='L' and initialpoint[0]>-1:
            initialpoint[0]-=1
    print(dicpart1[tuple(initialpoint)],end = '')
    
print("\nSecond part:")

dicpart2={
        (0,2):1,
        (-1,1):2,
        (0,1):3,
        (1,1):4,
        (-2,0):5,
        (-1,0):6,
        (0,0):7,
        (1,0):8,
        (2,0):9,
        (-1,-1):'A',
        (0,-1):'B',
        (1,-1):'C',
        (0,-2):'D'
        }
  
    
for i in data:
    initialpoint=[-2,0]
    for j in i[0]:
        if j=='U' and initialpoint[1]+abs(initialpoint[0])<2:
            initialpoint[1]+=1  
        elif j=='D' and initialpoint[1]-abs(initialpoint[0])>-2:
            initialpoint[1]-=1    
        elif j=='R'and initialpoint[0]+abs(initialpoint[1])<2:
            initialpoint[0]+=1
        elif j=='L' and initialpoint[0]-abs(initialpoint[1])>-2:
            initialpoint[0]-=1
    print(dicpart2[tuple(initialpoint)],end = '')
