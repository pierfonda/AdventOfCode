import re

with open("input.dat") as file:
    data = file.readlines()

#data=['R8, R4, R4, R8\n']
    
data = [re.split(' |, |\n',x) for x in data][0]
    
#print(data)
    
class circ(list):
    def __getitem__(self, idx):
        return super(circ, self).__getitem__(idx % len(self))

cardinals=circ(["N","E","S","W"])
carddir={"N":[0,1],"E":[1,0],"S":[0,-1],"W":[-1,0]}

posdir=[0,0,"N"];
nextind=0;
nextstep=0;
visitedlocations=[]

for i in range(len(data)-1):
    if data[i][0]=="R":
        nextind=+1
        nextstep=int(data[i][1:])
    elif data[i][0]=="L":
        nextind=-1
        nextstep=int(data[i][1:])
    else:
        break
    posdir[2]=cardinals[cardinals.index(posdir[2])+nextind]    
    for j in range(nextstep):
        newloc=[posdir[0]+(j+1)*carddir[posdir[2]][0],posdir[1]+(j+1)*carddir[posdir[2]][1]]
        if newloc in visitedlocations:
            print("Found already visited location at",newloc,"with distance",abs(newloc[0])+abs(newloc[1]),"(step",i,")")
        else:
            visitedlocations.append(newloc)
    posdir[0]+=nextstep*carddir[posdir[2]][0]    
    posdir[1]+=nextstep*carddir[posdir[2]][1]


print(posdir)
print(abs(posdir[0])+abs(posdir[1]))