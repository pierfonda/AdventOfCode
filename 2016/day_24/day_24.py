from queue import Queue
from itertools import permutations
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
            
def get_neighbours(p,g):
    dx, dy= len(g), len(g[0])
    nb=[]
    for i in  range(-1,2,2):
        if g[p[0]+i][p[1]]!='#' and p[0]+i>=0 and p[0]+i<dx:
            nb.append([p[0]+i,p[1]])        
        if g[p[0]][p[1]+i]!='#' and p[1]+i>=0 and p[1]+i<dy:
            nb.append([p[0],p[1]+i])
    return nb

def print_maze(g):
    dx, dy= len(g), len(g[0])
    m=np.zeros((dx,dy))
    for x in range(dx):
        for y in range(dy):
            if g[x][y]=='#':
                m[x][y]=0
            elif g[x][y]=='.':
                m[x][y]=1
            elif g[x][y].isnumeric():
                 m[x][y]=2#+int(g[x][y])
    plt.figure(figsize=(50,50))
    f = plt.imshow(m)
    f.axes.get_xaxis().set_visible(False)
    f.axes.get_yaxis().set_visible(False)
    
def find_shortest_path(s,e,g):
    ts=tuple(s)
    te=tuple(e)
    queue = Queue()
    visited = defaultdict(bool)
    visited[ts] = True
    queue.put([ts,0])
    while not queue.empty():
        pc,pd=queue.get()
        if pc==te:
            visited[pc]=True
            return pd
        for n in get_neighbours(list(pc),g):
            if visited[tuple(n)]:
                continue
            else:
                visited[tuple(n)]=True
                queue.put([tuple(n),pd+1])
    return 0

def find_global_path(s,rl,g):
    r=[]
    ds=defaultdict(int)
    for j in permutations(rl):
        safe=True
        if ds[(tuple(s),tuple(j[0]))]==0:
            d=find_shortest_path(s,j[0],g)
            ds[(tuple(s),tuple(j[0]))]=d
        else:
            d=ds[(tuple(s),tuple(j[0]))]
        for q in range(len(j)-1):
                if ds[(tuple(j[q]),tuple(j[q+1]))]==0:
                    pd=find_shortest_path(j[q],j[q+1],g)
                    d+=pd
                    ds[(tuple(j[q]),tuple(j[q+1]))]=pd
                else:
                    d+=ds[(tuple(j[q]),tuple(j[q+1]))]
                if len(r)>0 and d>r[1]:
                    safe=False
                    break
        if safe and len(r)>0 and d<r[1] or r==[]:
            r=[j,d]
            print(r)
    return [[s]+list(r[0]),r[1]]

def find_global_path_2(s,rl,g):
    r=[]
    ds=defaultdict(int)
    for j in permutations(rl):
        safe=True
        if ds[(tuple(s),tuple(j[0]))]==0:
            d=find_shortest_path(s,j[0],g)
            ds[(tuple(s),tuple(j[0]))]=d
        else:
            d=ds[(tuple(s),tuple(j[0]))]
        for q in range(len(j)-1):
                if ds[(tuple(j[q]),tuple(j[q+1]))]==0:
                    pd=find_shortest_path(j[q],j[q+1],g)
                    d+=pd
                    ds[(tuple(j[q]),tuple(j[q+1]))]=pd
                else:
                    d+=ds[(tuple(j[q]),tuple(j[q+1]))]
                if len(r)>0 and d>r[1]:
                    safe=False
                    break
        if ds[(tuple(j[-1]),tuple(s))]==0:
            pd=find_shortest_path(j[-1],s,g)
            ds[(tuple(j[-1]),tuple(s))]=pd
            d+=pd
        else:
            d+=ds[(tuple(j[-1]),tuple(s))]
        if safe and len(r)>0 and d<r[1] or r==[]:
            r=[j,d]
            print(r)
    return [[s]+list(r[0])+[s],r[1]]

with open("input.dat") as file:
    data = file.read().splitlines()
    
dimx, dimy = len(data), len(data[0])

grid=[[0 for y in range(dimy)] for x in range(dimx)]
robot_locations=[]
    
for x in range(dimx):
    for y in range(dimy):
        d=data[x][y]
        grid[x][y]=d
        if d=='0':
            startpos=[x,y]
        if d.isnumeric() and d!='0':
            robot_locations.append([x,y])
            
# print_maze(grid)

print(find_global_path(startpos,robot_locations,grid)[1])

print(find_global_path_2(startpos,robot_locations,grid)[1])