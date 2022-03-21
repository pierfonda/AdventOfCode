import numpy as np

input=289326

def get_coord(n):
    now=np.array([1,0,0])
    if n==1:
        return(now)
    c=1
    up=True
    while now[0]<n:
        for a in range(2):
            for x in range(c):
                sig=1 if c%2==1 else -1
                now+=[1,sig*int(up),sig*int(not(up))]
                if now[0]==n:
                    return(now)
            up=not(up)
        c+=1
        
def get_neighbours(p):
    nb=[]
    for i in  range(-1,2):
        for j in range(-1,2):
            n=[p[0]+i,p[1]+j]
            if n[0]!=p[0] or n[1]!=p[1]:
                nb.append(n)
    return nb
        
def get_value(n,vmax=0):
    sequence=np.expand_dims(np.array([1,0,0,1]), axis=0)
    for i in range(2,n+1):
        gc=get_coord(i)
        sequence=np.append(sequence,np.expand_dims(np.append(gc,0),axis=0),axis=0)
        for nb in get_neighbours(gc[1:3]):
            for q in sequence:
                if nb==q[1:3].tolist():
                    sequence[i-1,3]+=q[3]
        if vmax>0 and sequence[-1,3]>vmax:
            return(sequence[-1])
    return(sequence)

  
# out=get_coord(input)   
# print(abs(out[1])+abs(out[2]))

print(get_value(100000,input))
