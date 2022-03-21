with open("input.dat") as file:
    data = file.read().splitlines()

jmplist=[int(i) for i in data]

jmplist=[0,3,0,1,-3]

s,c=0,0
while c<len(jmplist):
    jump=jmplist[c]
    jmplist[c]+=1
    c+=jump
    s+=1
    # print(jmplist)

print(s)

jmplist=[int(i) for i in data]

# jmplist=[0,3,0,1,-3]

s,c=0,0
while c<len(jmplist):
    jump=jmplist[c]
    if jump>2:
        jmplist[c]-=1
    else:
        jmplist[c]+=1
    c+=jump
    s+=1
    # print(jmplist)
    
print(s)
