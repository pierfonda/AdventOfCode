import re
import numpy as np

def c(i):
    return '1' if (i=='#' or i==1 or i=='1') else '0' 

def rotoreflect(s):
    if len(s)==4:
        combos=['1234','2413','3142','4321','2143','3412']
        ret=[]
        for q in combos:
            ret.append(''.join([s[int(j)-1] for j in q]))
        return list(set(ret))
    elif len(s)==9:
        combos=['123456789','369258147','741852963','987654321','321654987','789456123','147258369','963852741']
        ret=[]
        for q in combos:
            ret.append(''.join([s[int(j)-1] for j in q]))
        return list(set(ret))
    else:   
        print(f"Error! Wrong string format {s}")
        
def to_grid(s):
    if np.mod(np.sqrt(len(s)),1)==0:
        side=int(np.sqrt(len(s)))
        return np.array([i for i in s]).reshape(side,side)
    else:
        print("Error! Non-square grid.")
        
def to_string(g):
    return ''.join(np.ndarray.flatten(g))

def generate_grid(g,dic):
    if len(set(g.shape))!=1:
        print("Error! Non-square grid.")
        return None
    if g.shape[0] % 2 == 0:
        l=g.shape[0]//2
        ret_g=np.zeros((3*l,3*l))
        for i in range(l):
            for j in range(l):
                ret_g[3*i:3*i+3,3*j:3*j+3]=to_grid(dic[to_string(g[2*i:2*i+2,2*j:2*j+2])])
        return np.vectorize(c)(ret_g)
    elif g.shape[0] % 3 ==0:
        l=g.shape[0]//3
        ret_g=np.zeros((4*l,4*l))
        for i in range(l):
            for j in range(l):
                ret_g[4*i:4*i+4,4*j:4*j+4]=to_grid(dic[to_string(g[3*i:3*i+3,3*j:3*j+3])])
        return np.vectorize(c)(ret_g)
    else:
        print(f"Error! I can't handle this dimension {g.shape}")
        return None
    
with open("input.dat") as file:
    data = file.read().splitlines()
    
data=[i.split() for i in data]

dic={}   
for d in data:
    base=''.join([c(i) for i in d[0] if i!='/'])
    rule=''.join([c(i) for i in d[2] if i!='/'])
    # print(base,rotoreflect(base))
    for b in rotoreflect(base):
        if b in dic:
            print(f"Error: asked to override existing rule! {dic[b]}, {rule}")
        dic[b]=rule    
    
print()

grid=to_grid(''.join([c(i) for i in '.#...####']))
print(grid,end='\n\n')
print(np.unique(grid,return_counts=True)[1][1],end='\n\n')

for i in range(18):
    grid=generate_grid(grid,dic)
    # print(grid,end='\n\n')
    print(f"Iteration {i+1}, lights on {np.unique(grid,return_counts=True)[1][1]}",end='\n\n')
