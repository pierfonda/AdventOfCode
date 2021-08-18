import hashlib
from collections import defaultdict
from queue import Queue

room_string={0:'U',1:'D',2:'L',3:'R'}
room_change={'U':[0,1],'D':[0,-1],'L':[-1,0],'R':[1,0]}

my_input='qtetzkpl'
#my_input='ihgpwlah'
#my_input='kglvqrro'
#my_input='ulqzkmiv'
#my_input='hijkl'

initial_position=[0,0]
grid_size=[4,4]

def get_hash(string):
    return ((hashlib.md5(string.encode())).hexdigest())[:4]

def check_door(char):
    if char.isnumeric() or char=='a':
        return False
    else:
        return True
    
def room_status(string):
    hsh=get_hash(string)
    o=[]
    for j in range(4):
        if check_door(hsh[j]):
            o.append(room_string[j])
    return o

def add_l(p,d):
    return [sum(x) for x in zip(p, d)]

def check_pos(p,d):
    pos=add_l(p, d)
    if pos[0]>=0 and pos[0]<grid_size[0] and pos[1]<=0 and pos[1]>-grid_size[1]:
        return True
    else:
        return False
    
def find_path(path,position):
    queue = Queue()
    visited = []
    
    queue.put((path,position))
    
    while not queue.empty():
        pa,po=queue.get()
        if po==[grid_size[0]-1,-grid_size[1]+1]:
#            print("Found:",pa[len(my_input):])
            visited.append(pa)
        for n in room_status(pa):
            if check_pos(po,room_change[n]) and pa not in visited: 
                queue.put((pa+n,add_l(po,room_change[n])))
#                print(pa+n,add_l(po,room_change[n]),TOTN)
    print(max([len(j) for j in visited])-len(my_input))

                
find_path(my_input,initial_position)