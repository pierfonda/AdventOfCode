import re,itertools

def partitioninteger(n,k,l=1):
    if k < 1:
        return
    if k == 1:
        if n >= l:
            yield (n,)
        return
    for i in range(l,n+1):
        for result in partitioninteger(n-i,k-1,i):
            yield (i,)+result

with open("input.dat") as file:
    data = file.readlines()
data = [x.strip() for x in data]

datalist=[]

for i in data:
    j=re.split(': |, | ',i)
    datalist.append([j[0],int(j[2]),int(j[4]),int(j[6]),int(j[8]),int(j[10])])

tot_spoon=100
calvalue=500

max_score=0
max_score_cal=0
for i in partitioninteger(tot_spoon,len(datalist)):
    for l in list(itertools.permutations(i)):
        tl=[0]*5
        total_score=1
        cal_flag=False
        for j in range(len(datalist)):
            for k in range(5):
                tl[k]+=l[j]*datalist[j][k+1] 
        if tl[4]==calvalue:
               cal_flag=True
        for k in range(4):
            tl[k]=max(0,tl[k])
            total_score=tl[k]*total_score
        if total_score>max_score:
            max_score=total_score
        if total_score>max_score_cal and cal_flag:
            max_score_cal=total_score
          

print(max_score,max_score_cal)