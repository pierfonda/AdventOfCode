import collections

with open("input.dat") as file:
    data = file.read().splitlines()

c,d=0,0
for i in data:
    j=collections.Counter(i.split())
    k=collections.Counter([''.join(sorted(u)) for u in i.split()])
    if len(j.keys())==len(i.split()):
        c+=1
    if len(k.keys())==len(i.split()):
            d+=1
        
print(c,d)