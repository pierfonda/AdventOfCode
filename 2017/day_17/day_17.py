step=370
# step=3

buffer=[0]
pos=0
insertions=2017
zeroprint=0

for i in range(1,insertions+1):
    pos=(pos+step+1) % i
    # print(f"The buffer is {buffer} of length {l} at position {cpos}. We need to make an insertion of value {i} after position {pos}.")
    if pos==0:
        print(i)
    if pos<i-1:
        buffer=buffer[:pos+1]+[i]+buffer[pos+1:]
    else:
        buffer=buffer[:pos+1]+[i]
    
print()

for i in range(1,len(buffer)):
    if buffer[i-1]==insertions:
        print(buffer[i-1],buffer[i])
        
# step=3
pos=0

for i in range(1,50000000):
    pos=(pos+step+1) % i
    if pos==0:
        print(i)