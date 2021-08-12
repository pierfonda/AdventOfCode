import itertools,sys

with open("input.dat") as file:
    data = file.readlines()
data = [x.strip() for x in data]    

thatsme="Pier"
namelist=[thatsme]
valuelist=[]

for i in data:
    j=i.split(" ")
    if j[0] not in namelist:
        namelist.append(j[0])
    if j[2]=="gain":
       valuelist.append([j[0],j[-1][:-1],int(j[3])]) 
    elif j[2]=="lose":
       valuelist.append([j[0],j[-1][:-1],-int(j[3])])

def happiness(a,b):    
    if a==thatsme or b==thatsme:
            return 0
    for l in valuelist:
        if l[0]==a and l[1]==b:
            return l[2]
        
#print(namelist)
#print(*valuelist,sep="\n")

permutations=list(itertools.permutations(namelist))
permutations=[list(i) for i in permutations]

print(len(permutations))

minhappy=sys.maxsize
maxhappy=0

for i in permutations:
    thappiness=0
    for j in range(len(i)):
        if j<len(i)-1:
           thappiness+=happiness(i[j],i[j+1])
           thappiness+=happiness(i[j+1],i[j])
        else:
            thappiness+=happiness(i[j],i[0])
            thappiness+=happiness(i[0],i[j])
    minhappy=min(minhappy,thappiness)
    maxhappy=max(maxhappy,thappiness)
        
print(maxhappy,minhappy)
