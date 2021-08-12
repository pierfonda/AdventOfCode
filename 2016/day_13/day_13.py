from copy import deepcopy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import LogNorm
import numpy as np

puzzle_input=1358
#puzzle_input=10

def is_wall(coord):
    x,y=coord
    b="{0:b}".format(x*x + 3*x + 2*x*y + y + y*y+puzzle_input)
    if str(b).count('1') % 2 ==0:
        return "o"
    else:
        return "w"
    
def is_wallb(coord):
    if is_wall(coord)=='w':
        return 1
    else:
        return 0
    
def print_maze(m):
    for j in range(len(m)):
        for i in range(len(m[j])):
            if [i,j]==start:
                print(f"  S",end='')
            elif [i,j]==end:
                print(f"  E",end='')
            elif is_wallb([i,j]):
                print(f"  #",end='')
            else:
                print(f"{m[i][j]:3}",end='')
        print('')

def make_step(k,sm,mz):
    for i in range(len(sm)):
        for j in range(len(sm[i])):
            if sm[i][j] == k:
                if i>0 and sm[i-1][j] == 0 and mz[i-1][j] == 0:
                    sm[i-1][j] = k + 1
                if j>0 and sm[i][j-1] == 0 and mz[i][j-1] == 0:
                    sm[i][j-1] = k + 1
                if i<len(sm)-1 and sm[i+1][j] == 0 and mz[i+1][j] == 0:
                    sm[i+1][j] = k + 1
                if j<len(sm[i])-1 and sm[i][j+1] == 0 and mz[i][j+1] == 0:
                    sm[i][j+1] = k + 1       
    return sm


start=[1,1]
end=[61,99]
maze_size=100

maze=[]
for i in range(maze_size):
    maze.append([])
    for j in range(maze_size):
        maze[i].append(is_wallb([i,j]))

#print_maze(maze)
        
solm=[]
for i in range(maze_size):
    solm.append([])
    for j in range(maze_size):
        solm[i].append(0)
        
solm[start[0]][start[1]]=1

k=1
while True:
    prevm=deepcopy(solm)
    solm=make_step(k,solm,maze)
    if solm[end[0]][end[1]]!=0:
        print("We reach the end in",solm[end[0]][end[1]]-1,"steps:")
        break
    if prevm==solm:
        break
    k+=1

solnm=np.array(solm)

print(len(solm))
               
plt.imshow(solnm, cmap=cm.hot, aspect='auto')
plt.colorbar()
plt.show()
    
#print_maze(solm)

count=0
for i in range(len(solm)):
    for j in range(len(solm[i])):
        if solm[i][j]>0 and solm[i][j]<100:
            count+=1
            
         
print(solm[start[0]][start[1]],solm[end[0]][end[1]],k,count)