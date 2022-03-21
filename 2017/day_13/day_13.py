from copy import deepcopy

with open("input.dat") as file:
    data = file.read().splitlines()
    
depth_dic={}
layers=0
for j in data:
    b=[int(i.strip(':')) for i in j.split()]
    depth_dic[b[0]]=b[1]
    layers=max(b[0],layers)
    
# depth_dic={0: 3,1: 2,4: 4,6: 4}
# layers=6
    
def one_move(scanner,depths,dirs):
    for i in range(layers+1):
        if scanner[i]!=-1:
            scanner[i]+=dirs[i]
            if scanner[i]==0 or scanner[i]==depth_dic[i]-1:
                dirs[i]=-dirs[i]
    return scanner, dirs

scanner=[0 if i in depth_dic else -1 for i in range(layers+1)]
directions=[1 for i in range(layers+1)]

now=0
damage=0
while now<layers+1:
    # print(now,scanner)
    if scanner[now]==0:
        # print("Hit!",now,depth_dic[now])
        damage+=now*depth_dic[now]
    scanner, directions = one_move(scanner,depth_dic,directions)
    now+=1
    
print(f"Part one: {damage}")

damage=1
j=0
start_scanner=[0 if i in depth_dic else -1 for i in range(layers+1)]
start_directions=[1 for i in range(layers+1)]

# while damage>0:
#     now=0
#     damage=0
#     scanner, directions = deepcopy(start_scanner), deepcopy(start_directions)
#     while now<layers+1:
#         if scanner[now]==0:
#             # print("Hit!",now,depth_dic[now])
#             damage+=max(now,1)*depth_dic[now]
#         scanner, directions = one_move(scanner,depth_dic,directions)
#         now+=1
#     if j % 1000 ==0:
#         print(j,damage)
#     start_scanner, start_directions = one_move(start_scanner,depth_dic,start_directions)
#     j+=1

found=False
n0=0
while not found:
    bad=False
    for i in depth_dic:
        if (n0+i)% (2*(depth_dic[i]-1))==0:
            bad=True
            break
    if not bad:
        found=True 
    n0+=1

print(f"Part two: {n0-1}")