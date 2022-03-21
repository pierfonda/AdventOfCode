with open("input.dat") as file:
    data = file.read().splitlines()

row_chcksum=[]
row_chcksum2=[]
for i in data:
    d=[int(j) for j in i.split()]
    for a in d:
        for b in d:
            if a != b and a%b==0:
                row_chcksum2.append(a/b)
    row_chcksum.append(max(d)-min(d))
    
print(sum(row_chcksum))
print(sum(row_chcksum2))
