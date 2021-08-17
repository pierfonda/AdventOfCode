import re

with open("input.dat") as file:
    data = file.read().splitlines()
    
machines=[]

#Structure of a disc info: [Disc #,npos,t0,pos0] 

for line in data:
    discd=re.split(" |#|=|\.|\,",line)
    machines.append([int(discd[2]),int(discd[4]),int(discd[8]),int(discd[14])])

machines.append([len(machines)+1,11,0,0])

level=0
in_t=-1

while level<len(machines):
    in_t+=1
    t=in_t
    level=0
    for i in range(len(machines)):
        t+=1
        if (t+machines[i][2]+machines[i][3])%machines[i][1]==0:
            level+=1
        else:
            break

print(in_t,level)
    

