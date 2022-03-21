with open("input.dat") as file:
    data = (file.read().split('\n')[0]).split(',')
    
# data='ne,ne,ne'.split(',')
# data='ne,ne,sw,sw'.split(',')
# data='ne,ne,s,s'.split(',')
# data='se,sw,se,sw,sw'.split(',')

maxd=0  
pos=[0,0,0]
for i in data:
    if i=='s':
        pos[0]-=1
        pos[2]+=1
    elif i=='sw':
        pos[0]-=1
        pos[1]+=1
    elif i=='nw':
        pos[1]+=1
        pos[2]-=1
    elif i=='n':
        pos[0]+=1
        pos[2]-=1
    elif i=='ne':
        pos[0]+=1
        pos[1]-=1
    elif i=='se':
        pos[1]-=1
        pos[2]+=1
    else:
        print("I do not understand!")
        break
    maxd=max(maxd,sum([abs(j) for j in pos])/2)
    # print(pos)
    
print(pos,sum([abs(j) for j in pos])/2,maxd)