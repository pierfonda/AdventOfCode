with open("input.dat") as file:
    data = list(file.read())

floor=0
index=0
    
for i in data:
    index+=1
    if i=='(':
        floor+=1
        print(index) if floor==-1 else None
    elif i==')':
        floor-=1
        print(index) if floor==-1 else None
        
print(floor)