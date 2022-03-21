import re

def prune(w,d):
    w=[i for i in w if i in d]
    for i in d:
        d[i]=[j for j in d[i] if j in w]
    d={k:v for k,v in d.items() if v}
    return w,d

def check_weight(w,d,we):
    for i in d:
        wel=[we[j] for j in d[i] if j not in d]
        if len(set(wel))==1 and len(wel)>0:
            we[i]+=len(wel)*wel[0]
        elif len(wel)!=0:
            print("Misplaced weight at",i,":",d[i],wel)

with open("example.dat") as file:
    data = file.read().splitlines()
    
with open("input.dat") as file:
    data = file.read().splitlines()
    
dic, weights, words = {}, {}, []
for i in data:
    d=list(filter(len,re.split('\W',i)))
    words.append(d[0])
    weights[d[0]]=int(d[1].strip('()'))
    if len(d)>2:
        dic[d[0]]=d[2:]
        
# print(weights['vrgxe'],weights['vrgxe']-2166+2159)
# weights['vrgxe']=weights['vrgxe']-2166+2159
        
while len(words)>1:
    check_weight(words,dic,weights)
    words, dic = prune(words,dic)

print("The bottom tower is:",words[0])
