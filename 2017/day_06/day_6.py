from copy import deepcopy

with open("input.dat") as file:
    data = file.read().split()

d=[int(i) for i in data]

# d=[0,2,7,0]

n=1
c=0
states=[deepcopy(d)]
while True:
    m=d.index(max(d))
    r=d[m]
    d[m]=0
    for i in range(r):
        nxt= (m+i+1) % len(d)
        d[nxt]+=1
    if d not in states:
        states.append(deepcopy(d))
    elif c==0:
        n1=n
        states=states[-1]
        c+=1
    else:
        break
    # print(n,d)
    n+=1

print(n,n1,n-n1-1)