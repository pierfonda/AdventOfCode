with open("input.dat") as f:
    for line in f:
        if 'Begin' in line:
            start=line[-3]
        elif 'Perform' in line:
            check=int(line.split()[5])
            
# def next_move_example(pos,ones):
#     if pos[0] not in ones:
#         value=0
#     else:
#         value=1
#     if pos[1]=='A':
#         if value==0:
#             ones.append(pos[0])
#             pos[0]=pos[0]+1
#             pos[1]='B'
#         else:
#             ones.remove(pos[0])
#             pos[0]=pos[0]-1
#             pos[1]='B'
#     elif pos[1]=='B':
#         if value==0:
#             ones.append(pos[0])
#             pos[0]=pos[0]-1
#             pos[1]='A'
#         else:
#             pos[0]=pos[0]+1
#             pos[1]='A'
#     return pos,sorted(ones)

def next_move(pos,ones):
    if pos[0] not in ones:
        value=0
    else:
        value=1
    if pos[1]=='A':
        if value==0:
            ones[pos[0]]=1
            pos[0]=pos[0]+1
            pos[1]='B'
        else:
            ones.pop(pos[0])
            pos[0]=pos[0]-1
            pos[1]='D'
    elif pos[1]=='B':
        if value==0:
            ones[pos[0]]=1
            pos[0]=pos[0]+1
            pos[1]='C'
        else:
            ones.pop(pos[0])
            pos[0]=pos[0]+1
            pos[1]='F'
    elif pos[1]=='C':
        if value==0:
            ones[pos[0]]=1
            pos[0]=pos[0]-1
            pos[1]='C'
        else:
            pos[0]=pos[0]-1
            pos[1]='A'
    elif pos[1]=='D':
        if value==0:
            pos[0]=pos[0]-1
            pos[1]='E'
        else:
            pos[0]=pos[0]+1
            pos[1]='A'
    elif pos[1]=='E':
        if value==0:
            ones[pos[0]]=1
            pos[0]=pos[0]-1
            pos[1]='A'
        else:
            ones.pop(pos[0])
            pos[0]=pos[0]+1
            pos[1]='B'
    elif pos[1]=='F':
        if value==0:
            pos[0]=pos[0]+1
            pos[1]='C'
        else:
            ones.pop(pos[0])
            pos[0]=pos[0]+1
            pos[1]='E'
    return pos,ones

cur=[0,start]
ones={}

for i in range(check):
    # print(cur,ones)
    if i % (check//100) ==0:
        print(f"{i/check*100:.4f}")
    cur, ones = next_move(cur,ones)
    
print(len(ones))