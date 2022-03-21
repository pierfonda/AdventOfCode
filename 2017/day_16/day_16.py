import re,copy

with open("input.dat") as file:
    data = re.split(',|\n',file.read())[:-1]
    
def dance(op,string):
    if op[0]=='s':
        l=int(op[1:])
        return string[-l:]+string[:-l]
    if op[0]=='x':
        vals=[int(i) for i in op[1:].split('/')]
        lstr=[i for i in string]
        lstr[vals[0]],lstr[vals[1]]=lstr[vals[1]],lstr[vals[0]]
        return ''.join(lstr)
    if op[0]=='p':
        lstr=[i for i in string]
        vals=[lstr.index(i) for i in op[1:].split('/')]
        lstr[vals[0]],lstr[vals[1]]=lstr[vals[1]],lstr[vals[0]]
        return ''.join(lstr)


programs = 'abcdefghijklmnop'
# programs='abcde'
# data=['s1','x3/4','pe/b']

po=copy.deepcopy(programs)
l=len(po)

for i in data:
    programs=dance(i,programs)
    
print(programs)
    
dic={programs.index(i):po.index(i) for i in po}
pb=copy.deepcopy(po)

n=0
while True:
    print(n,pb)
    for i in data:
        pb=dance(i,pb)
    # pb=''.join([pb[dic[i]] for i in range(l)])
    n+=1
    if pb==po:
        break

print()
tot=10**9        
print(n,tot%n)