with open("input.dat") as file:
    data = file.read().splitlines()
    
def rotate(l, n):
    return l[-(n%len(l)):] + l[:-(n%len(l))]

def do_instruction(instruction,pwd):
    lpwd=list(pwd)
    s=instruction.split(' ')
    if s[0]=='rotate':
        if s[1]=='left':
            lpwd=rotate(lpwd,-int(s[2]))
        elif s[1]=='right':
            lpwd=rotate(lpwd,int(s[2]))
        elif s[1]=='based':
            if lpwd.index(s[6])>=4:
                r=2+lpwd.index(s[6])  
            else:
                r=1+lpwd.index(s[6])
            lpwd=rotate(lpwd,r)
    elif s[0]=='swap':
        if s[1]=='position':
            vX,vY=lpwd[int(s[2])],lpwd[int(s[5])]
            lpwd[int(s[2])]=vY
            lpwd[int(s[5])]=vX
        elif s[1]=='letter':
            X,Y=lpwd.index(s[2]),lpwd.index(s[5])
            lpwd[X]=s[5]
            lpwd[Y]=s[2]
    elif s[0]=='move':
        X,Y=int(s[2]),int(s[5])
        t=lpwd[X]
        lpwd.remove(t)
        lpwd.insert(Y,t)
    elif s[0]=='reverse':
        X,Y=int(s[2]),int(s[4])
        rev=[]
        for i in range(X,Y+1):
            rev.append(lpwd[i])
        rev.reverse()
        for i in range(len(rev)):
            lpwd[X+i]=rev[i]
    return ''.join(lpwd)
    
pwd='abcdefgh'
        
for j in data:
    pwd=do_instruction(j,pwd)
    
from itertools import permutations

scrambled='fbgdceah'

for p in permutations(scrambled):
    pwd=p
    for j in data:
        pwd=do_instruction(j,pwd)
    if pwd==scrambled:
        print(''.join(p))
        break