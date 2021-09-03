import re

with open("input.dat") as file:
    data = file.readlines()
    
#data = [re.split('\n',x) for x in data]
data = [list(x)[:-1] for x in data]

data=list(map(list, zip(*data)))

def most_frequent(List):
    return max(set(List), key = List.count)

def less_frequent(List):
    return min(set(List), key = List.count)

for i in data:
    print(most_frequent(i),end="")

print("")

for i in data:
    print(less_frequent(i),end="")