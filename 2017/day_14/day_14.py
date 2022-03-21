import numpy as np

def knot_hash(string):
    to_process=[ord(i) for i in string]
    to_process+=[17,31,73,47,23]
    b=256
    cur_pos=0
    skip_size=0
    tl=list(range(b))
    for x in range(64):
        for i in to_process:
            tr=[tl[(cur_pos+j)% b] for j in range(i)]
            for j in range(i):
                tl[(cur_pos+j)% b] = tr[i-j-1]
            cur_pos=(cur_pos+i+skip_size)%b
            skip_size+=1
    hsh=[]
    for a in range(16):
        c=tl[16*a]
        for b in range(1,16):
            c=c^tl[16*a+b]
        hsh.append(c)
    return ''.join([format(i,'#010b')[2:] for i in hsh])

def label_components(array):
    sizes=array.shape
    n_domains=0
    for (i,j),v in np.ndenumerate(array):
        if v!=0:
            if (i==0 or array[i-1,j]==0) and (j==0 or array[i,j-1]==0):
                n_domains+=1
                array[i,j]=n_domains
            elif (i>0 and array[i-1,j]!=0):
                array[i,j]=array[i-1,j]
            elif (j>0 and array[i,j-1]!=0):
                array[i,j]=array[i,j-1]
    for (i,j),v in np.ndenumerate(array):
        if v!=0:
            if (i>0 and array[i-1,j]!=0 and array[i,j]!=array[i-1,j]):
                array=np.where(array==array[i,j],array[i-1,j],array)
            if (j>0 and array[i,j-1]!=0 and array[i,j]!=array[i,j-1]):
                array=np.where(array==array[i,j],array[i,j-1],array)
            if (i<sizes[0]-1 and array[i+1,j]!=0 and array[i,j]!=array[i+1,j]):
                array=np.where(array==array[i,j],array[i+1,j],array)
            if (j>sizes[1]-1 and array[i,j+1]!=0 and array[i,j]!=array[i,j+1]):
                array=np.where(array==array[i,j],array[i,j+1],array)
    values=sorted(list(set(array.flatten()))) 
    n_domains=0
    for i in values:
        array=np.where(array==i,n_domains,array)
        n_domains+=1
    return array, sorted(list(set(array.flatten()))) 
    
input_string='vbqugkhl'
# input_string='flqrgnkx'

rows=128
found=0
array=np.zeros((rows,rows))

for i in range(rows):
    curr=knot_hash(input_string+'-'+str(i))
    array[i]=[int(i) for i in curr[:rows]]
    # array.append()
    found+=curr.count('1')
    
print(found)
    
array,values =label_components(array)

print(max(values))


