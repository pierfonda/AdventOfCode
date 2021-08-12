from collections import Counter
from itertools import combinations

with open("input.dat") as file:
    data = file.readlines()
data = [int(x.strip()) for x in data]

#data=[20, 15, 10, 5,  5]

eggnog=150
unsrt_cmb=[]
srt_comb=[]

def fill_it(liters,datatemp,datafull):
    if datatemp:
        for i in datatemp:
            if liters-i==0:
                unsrt_comb.append(list((Counter(datafull)-(Counter(datatemp)-Counter([i]))).elements()))
            elif liters-i>0:
                fill_it(liters-i,list((Counter(datatemp)-Counter([i])).elements()),datafull)
      
#fill_it(eggnog,data,data)

#for i in unsrt_comb:
#    i.sort()
#    if i not in srt_comb:
#        srt_comb.append(i)

#print(srt_comb)

count=0
ncount=[]
for nc in range(len(data),1,-1):
    for c in combinations(data,nc):
        if sum(c)==eggnog:
            count +=1
            ncount.append(len(c))

print(count)          
print(ncount.count(min(ncount)))