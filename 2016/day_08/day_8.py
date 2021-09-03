import matplotlib.pyplot as plt
from matplotlib import colors
import re


# Rect function
def rect(matr,rec):
    for x in range(rec[0]):
        for y in range(rec[1]):
            matr[y][x]=1
            
# Rotate function
def rota(matr,coord,pos,shift):
    if coord=='x':
        matr[pos]=matr[pos][-shift:]+matr[pos][:-shift]
    elif coord=='y': 
        test=[list(x) for x in list(zip(*matr))]
        test[pos]=test[pos][-shift:]+test[pos][:-shift]
        matr[:]=[list(x) for x in list(zip(*test))]
    else:
        print("Wrong coordinate name.")

# Load data
with open("input.dat") as file:
    data = file.read().splitlines()
data = [x.strip() for x in data]    
    
Nx = 50
Ny = 6
    
screen = [ [ 0 for i in range(Nx) ] for j in range(Ny) ] 

for i in data:
    line=re.split(' |=|x',i)
    if line[0]=='rotate':
        if line[1]=='column':
            rota(screen,'y',int(line[-3]),int(line[-1]))
        elif line[1]=='row':
            rota(screen,'x',int(line[-3]),int(line[-1]))
    elif line[0]=='rect':
        rect(screen,[int(line[1]),int(line[2])])
        
toton=0
for x in range(Nx):
    for y in range(Ny):
        toton+=screen[y][x]

print(toton)
    
cmap = colors.ListedColormap(['gray', 'yellow'])

fig, ax = plt.subplots()
ax.imshow(screen, cmap=cmap,vmin=0, vmax=1,interpolation='none')
ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=1)
ax.set_xticks(range(Nx))
ax.set_yticks(range(Ny))

#plt.colorbar()
plt.show()