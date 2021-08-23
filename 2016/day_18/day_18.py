from matplotlib import pyplot as plt

with open("input.dat") as file:
    data = file.read()
    
#data='.^^.^.^^^^A'

first_row=[x for x in data][:-1]
for i in range(len(first_row)):
    first_row[i]=0 if first_row[i]=='.' else 1
  
#Rules:
# 1*0 --> 1
# 0*1 --> 1 
    

def get_row(prev_row):
    l=len(prev_row)
    o=[]
    for i in range(l):
        left=0 if i==0 else prev_row[i-1]
        right=0 if i==l-1 else prev_row[i+1]
        o.append(left^right)
    return o

r=first_row
safe_tiles=0
row_tiles=[]
for i in range(400000):
    safe_tiles_row=0
    for k in r:
        if k==0:
            safe_tiles+=1
            safe_tiles_row+=1
#    print(''.join(r))
    row_tiles.append(safe_tiles_row)
    r=get_row(r)

print(safe_tiles)

#plt.plot(row_tiles)
#plt.show()