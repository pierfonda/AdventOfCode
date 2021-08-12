from itertools import combinations

with open("input.dat") as file:
    data = file.readlines()
data = [int(x.strip()) for x in data]

group_size=int(sum(data)/4)

n=0
products=[]

def prod(myList):
    result = 1
    for x in myList:
         result = result * x 
    return result 

for j in combinations(data,5):
    if sum(j)==group_size:
        products.append(prod(j))
#        for k in combinations([x for x in data if x not in j],8):
#           if sum(k)==group_size:
#               print(j,k,[x for x in data if x not in j and x not in k])
        
products.sort()
print(products[0])