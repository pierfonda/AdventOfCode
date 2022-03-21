with open("input.dat") as file:
    data = file.read().split('\n')[0]
    data = [int(i) for i in data.split(',')]
    
# data=[3,4,1,5]
b=256
tl=list(range(b))

cur_pos=0
skip_size=0

for i in data:
    tr=[tl[(cur_pos+j)% b] for j in range(i)]
    for j in range(i):
        tl[(cur_pos+j)% b] = tr[i-j-1]
    cur_pos=(cur_pos+i+skip_size)%b
    skip_size+=1
print(skip_size,cur_pos,tl[0]*tl[1])

with open("input.dat") as file:
    data = file.read().split('\n')[0]
    # data='1,2,4'
    data=[ord(i) for i in data]
    
data+=[17,31,73,47,23]
# print(data)

cur_pos=0
skip_size=0
tl=list(range(b))

for x in range(64):
    for i in data:
        tr=[tl[(cur_pos+j)% b] for j in range(i)]
        for j in range(i):
            tl[(cur_pos+j)% b] = tr[i-j-1]
        cur_pos=(cur_pos+i+skip_size)%b
        skip_size+=1
    # print(skip_size,cur_pos,tl[0]*tl[1])
    
hsh=[]
for a in range(16):
    c=tl[16*a]
    for b in range(1,16):
        c=c^tl[16*a+b]
    hsh.append(c)
    
# hsh=[64, 7, 255]
    
for i in hsh:
    if len(str(hex(i)))==4:
         print(hex(i)[2:],end='')
    else:
        print('0'+hex(i)[2:],end='')
    
