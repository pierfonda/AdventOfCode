from heapq import heappop, heappush

with open("input.dat") as file:
    data = file.read().splitlines()

dic={}

for i in data:
    c=i.split()
    b=int(c[0])
    # print(c)
    t=[int(j.strip(',')) for j in c[2:]]
    # print(b,t)
    if b not in dic:
        dic[b]=list(set(sorted(t)))
    else:
        dic[b]=list(set(sorted(dic[b]+t)))
    for tt in t:
        if tt not in dic:
            dic[tt]=[b]
        else:
            dic[tt]=list(set(sorted(dic[tt]+[b])))

groups=[]
for i in dic:
    frontier,visited=[],[]
    heappush(frontier,i)
    while len(frontier)>0:
        current = heappop(frontier)
        for prox in dic[current]:
            if prox not in visited:
                heappush(frontier,prox)
                visited.append(prox)
    visited=list(set(sorted(visited)))
    if visited not in groups:
        groups.append(visited)

print(len(groups))
 
for i in groups:
    if 0 in i:
        print(len(i))
