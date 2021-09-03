#import random
#import numpy as np
import matplotlib.pyplot as plt

# Switch off function
def swoff(matr,xI,xF):
    for i in range(xI[0],xF[0]+1):
        for j in range(xI[1],xF[1]+1):
            matr[i][j]=0

# Switch on function
def swon(matr,xI,xF):
    for i in range(xI[0],xF[0]+1):
        for j in range(xI[1],xF[1]+1):
            matr[i][j]=1
            
# Toggle function
def stoggle(matr,xI,xF):
    for i in range(xI[0],xF[0]+1):
        for j in range(xI[1],xF[1]+1):
            matr[i][j]= abs(1-matr[i][j])   
            
# Switch off function part 2
def swoff2(matr,xI,xF):
    for i in range(xI[0],xF[0]+1):
        for j in range(xI[1],xF[1]+1):
            matr[i][j]=max(0,matr[i][j]-1)

# Switch on function part 2
def swon2(matr,xI,xF):
    for i in range(xI[0],xF[0]+1):
        for j in range(xI[1],xF[1]+1):
            matr[i][j]+=1
            
# Toggle function part 2
def stoggle2(matr,xI,xF):
    for i in range(xI[0],xF[0]+1):
        for j in range(xI[1],xF[1]+1):
            matr[i][j]+=2

# Exectute instruction  function (formatted as in the input file)
def execute_instruction(line,matr):
    tmpstr=line.split(" ")
    if tmpstr[0]=='toggle':
        xI=[int(y) for y in tmpstr[1].split(",")]
        xF=[int(y) for y in tmpstr[3].split(",")]
        stoggle(matr,xI,xF)
    elif tmpstr[0]=='turn' and tmpstr[1]=='on':
        xI=[int(y) for y in tmpstr[2].split(",")]
        xF=[int(y) for y in tmpstr[4].split(",")]
        swon(matr,xI,xF)
    elif tmpstr[0]=='turn' and tmpstr[1]=='off':
        xI=[int(y) for y in tmpstr[2].split(",")]
        xF=[int(y) for y in tmpstr[4].split(",")]
        swoff(matr,xI,xF)
    else:
        print("Not valid")

# Exectute instruction function for part 2 (formatted as in the input file)
def execute_instruction2(line,matr):
    tmpstr=line.split(" ")
    if tmpstr[0]=='toggle':
        xI=[int(y) for y in tmpstr[1].split(",")]
        xF=[int(y) for y in tmpstr[3].split(",")]
        stoggle2(matr,xI,xF)
    elif tmpstr[0]=='turn' and tmpstr[1]=='on':
        xI=[int(y) for y in tmpstr[2].split(",")]
        xF=[int(y) for y in tmpstr[4].split(",")]
        swon2(matr,xI,xF)
    elif tmpstr[0]=='turn' and tmpstr[1]=='off':
        xI=[int(y) for y in tmpstr[2].split(",")]
        xF=[int(y) for y in tmpstr[4].split(",")]
        swoff2(matr,xI,xF)
    else:
        print("Not valid")

# Load data
with open("input.dat") as file:
    data = file.readlines()
data = [x.strip() for x in data]    

N = 1000
M = 1000

# Initialize matrix
lights = [ [ 0 for i in range(M) ] for j in range(N) ] 

for i in range(len(data)):,
     execute_instruction(data[i],lights)
#    plt.imshow(lights)
#    plt.colorbar()
#    plt.imsave('test'+str(i).zfill(6)+'.png',lights)

totlights=0
for i in range(M):
    for j in range(N):
        if lights[i][j]!=0:
            totlights+=1
        
print(totlights)

# Re-initialize matrix for second run
lights = [ [ 0 for i in range(M) ] for j in range(N) ] 

for i in range(len(data)):
     execute_instruction2(data[i],lights)
#    plt.imshow(lights, vmin=0, vmax=50, cmap='jet')
#    plt.colorbar()
     plt.imsave('secondtest'+str(i).zfill(6)+'.png',lights, vmin=0, vmax=50, cmap='jet')
  
plt.imshow(lights)
plt.colorbar()
plt.show()

totlights=0
for i in range(M):
    for j in range(N):
        if lights[i][j]!=0:
            totlights+=lights[i][j]
        
print(totlights)