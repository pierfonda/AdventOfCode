import numpy as np

with open("input.dat") as file:
    data = [[j for j in i.strip('\n')] for i in file.readlines()]
  
def gd(d,c):
    return d[c[0]][c[1]]

start=False
chars=[]
for i in range(len(data)):
    for j in range(len(data[i])):
        if gd(data,[i,j])!=' ' and not start:
            start=[i,j]
        if gd(data,[i,j]) not in chars:
            chars.append(data[i][j]) 
    
# for i in data:
#     print(''.join(i))
    
movdirs=np.array([[1,0],[-1,0],[0,1],[0,-1]])

cur=np.array(start)
foundchars=[]
movdir=np.array([1,0])
i=1

print()

while True:
    # print(cur,gd(data,cur))
    if gd(data,cur+movdir)=='+':
        movpool=movdirs[~((movdirs[:,0]==-movdir[0]) * (movdirs[:,1]==-movdir[1]))]
        for j in movpool:
            n=cur+movdir+j
            if 0<n[0]<len(data) and 0<n[1]<len(data[0]):
                # print(f"\t{cur}, {cur+movdir}, {n}, {gd(data,n)}")
                if gd(data,n)!=' ':
                    cur+=movdir
                    movdir=j
                    break
    elif gd(data,cur+movdir).isalpha():
        foundchars.append(gd(data,cur+movdir))
        cur+=movdir
    elif gd(data,cur+movdir)!=' ':
        cur=cur+movdir
    else:
        print(f"I don't know where to go: from {cur}-->{cur+movdir} i.e. {gd(data,cur)} --> {gd(data,cur+movdir)}")
        break
    i+=1
    
print()
print(f"I did {i} steps and found {''.join(foundchars)} letters.")
