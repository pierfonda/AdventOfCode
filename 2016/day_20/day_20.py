with open("input.dat") as file:
    data = file.read().splitlines()

intervals=[]

for j in data:
    intervals.append([int(q) for q in j.split('-')])

for j in range(len(intervals)):
    ij=intervals[j]
    if ij[0]>ij[1]:
        intervals[j]=[ij[1],ij[0]]
    
intervals=sorted(intervals)
        
has_changed=True

while has_changed:
    has_changed=False
    for j in range(len(intervals)):
        if j<len(intervals)-2 and intervals[j][1]>=intervals[j+1][0]-1:
            to_add=[intervals[j][0],max(intervals[j+1][1],intervals[j][1])]
            to_remove=[intervals[j],intervals[j+1]]
            for q in to_remove:
                intervals.remove(q)
            intervals.append(to_add)
            intervals=sorted(intervals)
            has_changed=True
    
print(intervals[0][1]+1)

mininterval,maxinterval = min([q[0] for q in intervals]), max([q[1] for q in intervals])

tot_ip=0
for q in range(len(intervals)-2):
    tot_ip+=intervals[q+1][0]-intervals[q][1]-1

print(tot_ip)    