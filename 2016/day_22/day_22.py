import matplotlib.pyplot as plt

#from itertools import combinations_with_replacement as cwr
from itertools import permutations

def minmax(it):
    min = max = None
    for val in it:
        if min is None or val < min:
            min = val
        if max is None or val > max:
            max = val
    return min, max

with open("input.dat") as file:
    data = file.read().splitlines()

disk_structure=[]

for i in data[2:]:
    li=i.split()
    x,y = int(li[0].split('-')[1][1:]),int(li[0].split('-')[2][1:])
    size,used,avail,use = int(li[1][:-1]), int(li[2][:-1]) , int(li[3][:-1]), int(li[4][:-1])/100
    disk_structure.append([[x,y],size,used,avail,use])
#    print(li,disk_structure[-1])

viable_pairs=0
for i in permutations(disk_structure,2):
    ai=list(i)[0]
    bi=list(i)[1]
    if ai[2]!=0 and ai[0]!=bi[0] and ai[2]<=bi[3]:
        viable_pairs+=1
        
print(viable_pairs)
        
start_node,goal_node=disk_structure[:2]

for i in disk_structure:
    if i[0][0]<=start_node[0][0] and i[0][1]<=start_node[0][1]:
        start_node=i
    if  i[0][0]>=goal_node[0][0] and i[0][1]==0:
        goal_node=i
        
print(start_node,goal_node)

xmin,xmax= minmax([i[0][0] for i in disk_structure])
ymin,ymax= minmax([i[0][1] for i in disk_structure])

ndarray=[[0 for x in range(xmax)] for y in range(ymax)]

for x in range(xmax):
    for y in range(ymax):
        found=False
        for i in disk_structure:
            if i[0]==[x,y]:
                ndarray[y][x]=i[1:]
                found=True
        if not found:
            ndarray[y][x]=0
                    
print(17+22+37+36*5)
        
plt.imshow([[ndarray[y][x][3] for x in range(xmax)] for y in range(ymax)])
plt.colorbar()
plt.show()
