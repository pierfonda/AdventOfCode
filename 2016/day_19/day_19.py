import math  
from matplotlib import pyplot as plt


class circ(list):
    def __getitem__(self, idx):
        return super(circ, self).__getitem__(idx % len(self))
    
def get_survivor(n):
    e=circ([[i+1,1] for i in range(n)])
    i=0
    while len(e)>1:
#        print(i,e[i],e)
        if e[i][1]!=0 and e[i][0]!=e[i+1][0]:
            e[i][1]+=e[i+1][1]
            e[i+1][1]=0
        else:
            e.remove(e[i])
            i=(i-1) % len(e)
        i=(i+1)%len(e)
    return e[0]

def highestPowerof2(n):
    res = 0;
    for i in range(n, 0, -1):
        if ((i & (i - 1)) == 0):
            res = i;
            break;
    return res;

def hP3(n):
    q=0
    while 3**q<n:
        q+=1
    return q;

def get_survivor_2(n):
    return 1+2*(n-highestPowerof2(n))

def get_survivor_3(n):
    e=circ([i+1 for i in range(n)])
    i=0
    while len(e)>1:
        ne=len(e)
        o=(i+math.floor(len(e)/2))%ne
        s=e[i]
#        print(f"Indexes: ({i} -> {o}) Values: ({e[i]} -> {e[o]}) Chain length: {ne}, Total {e}")
        e.remove(e[o])
        i=e.index(s)+1
    return e[0]

def get_survivor_4(n):
    bn=hP3(n)
    if n-3**(bn-1) <= 3**(bn-1):
        return n-3**(bn-1)
    else:
        return None

print(get_survivor_2(3017957))

#for j in range(1,100,1):
#    print(j,get_survivor_3(j),get_survivor_4(j))
#    
print(get_survivor_4(3017957))
    
#plt.plot([get_survivor_3(j) for j in range(1,500)])
#plt.show()