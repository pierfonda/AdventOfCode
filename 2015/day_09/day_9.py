import itertools,sys

with open("input.dat") as file:
    data = file.readlines()
data = [x.strip() for x in data]

names=[]
distlist=[]

for i in range(len(data)):
    j=data[i].split()
    distlist.append([j[0],j[2],int(j[4])])
    if j[0] not in names:
        names.append(j[0])
    elif j[2] not in names:
        names.append(j[2])
        
def distance(a,b):
    for l in distlist:
        if l[0]==a and l[1]==b:
            return l[2]
        elif l[1]==a and l[0]==b:
            return l[2]

permutations=list(itertools.permutations(names))
permutations=[list(i) for i in permutations]

mindist=sys.maxsize
maxdist=0
for i in permutations:
    tdist=0
    for j in range(len(i)-1):
        tdist+=distance(i[j],i[j+1])
    mindist=min(mindist,tdist)
    maxdist=max(maxdist,tdist)
        
print("The minimal distance is",mindist)
print("The maximal distance is",maxdist)