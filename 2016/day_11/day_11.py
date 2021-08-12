from queue import Queue
from copy import deepcopy
from collections import defaultdict
from itertools import combinations
from timeit import default_timer as timer

with open("input.dat") as file:
    data = file.read().splitlines()
    
data.append("The first floor contains a an elerium generator, an elerium-compatible microchip, a dilithium generator, a dilithium-compatible microchip.")
    
floors={'first':0,'second':1,'third':2,'fourth':3}
namelen=3
status=[set() for i in floors]
all_objects=set()

for d in data:
    ld=d.split()
    for i in range(len(ld)):
        if 'floor' in ld[i]:
            floor=floors[ld[i-1]]
        if 'microchip' in ld[i]:
            status[floor].add(ld[i-1][:namelen].upper()+'-M')
            all_objects.add(ld[i-1][:namelen].upper()+'-M')
        if 'generator' in ld[i]:
             status[floor].add(ld[i-1][:namelen].upper()+'-G')
             all_objects.add(ld[i-1][:namelen].upper()+'-G')

all_objects=sorted(all_objects)

def print_status(status,elevator):
    if status != None:
        print(''.join(["-" for i in range(8*(len(all_objects)+2))]))
        for i in range(len(status)-1,-1,-1):
            print(f'F{i+1}',end='')
            if i==elevator:
                print('\tE',end='')
            else:
                print('\t*',end='')     
            for j in all_objects:
                if j in status[i]:
                    print('\t'+j,end='')
                else:
                    print('\t.',end='')
            print('')
            print(''.join(["-" for i in range(8*(len(all_objects)+2))]))
        print('')
        
def check_floor(floor):
    M= { i[:namelen] for i in floor if i[-1]=='M'}
    G= { i[:namelen] for i in floor if i[-1]=='G'}
    if len(G)==0 or len(M-G)==0:
        return True
    else:
        return False
     
# It is all in the hash: if we can prune the tree than it will become unfathomably faster.
#def floor_to_string(s,e):
#    st=''
#    for floor in s:
#        st+='|'
#        M= { i[:namelen] for i in floor if i[-1]=='M'}
#        G= { i[:namelen] for i in floor if i[-1]=='G'}
#        st+=f"{[len(M&G)]}"
#        for m in sorted(floor):
#            if m[:namelen] not in M or m[:namelen] not in G: 
#                st+=m+'-'
#    return st+'E:'+str(e) 

def floor_to_string(s,e):
    st=''
    for a in range(len(s)):
        for b in range(len(s)):
            M= { i[:namelen] for i in s[a] if i[-1]=='M'}
            G= { i[:namelen] for i in s[b] if i[-1]=='G'}
            st+=f"{[len(M&G)]}{a}{b}"
    return st+'E:'+str(e) 
    
def elevator_moves(s,e):
    return [ e+i for i in [1,-1] if -1<e+i<len(s) and -1<e<len(s)]

def find_moves(s,e):
    queue = Queue()
    visited = defaultdict(bool) 
    
    visited[floor_to_string(s,e)]=True
    
    queue.put((s,e,0))
    mazinga=0
        
    while not queue.empty():
        s,e,n=queue.get()

        if len(s[-1])==len(all_objects):
            print("All objects in the upper floor after",n," steps.")
            return n
        
        if n>mazinga:
            mazinga=n
            print(mazinga,end=' ')
        
        for i in (1,2):
            for p in combinations(s[e],i):
                for ep in elevator_moves(s,e):
                    if ep<e and all([len(s[x])==0 for x in range(ep+1)]):
                        continue
                    new_status=deepcopy(s)
                    for j in p:
                        new_status[e].remove(j)
                        new_status[ep].add(j)
                    if not check_floor(new_status[ep]) or not check_floor(new_status[e]):
                        #print(f"Invalid floor: {new_status[ep]}")
                        continue       
                    if visited[floor_to_string(new_status,ep)]:
                        continue
                    else:
                        if len(new_status[-1])==len(all_objects):
                            print_status(s,e)
                            print(f"Moving {p} from {e} to {ep}, at step {n} from start and having visited {len(visited)} configurations so far.\n")
                            print_status(new_status,ep)
                        #print(len(new_status[-1]),len(visited),n)
                        queue.put((new_status,ep,n+1))
                        visited[floor_to_string(new_status,ep)]=True
        if n>100:
            return n
    print(len(visited),"a",end='')
    return(n)
    
print_status(status,0)

start = timer()
n=find_moves(status,0)
stop = timer()

print("Elapsed time = {:.2f} s".format(((stop-start))))