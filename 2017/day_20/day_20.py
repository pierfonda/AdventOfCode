import re
import numpy as np

def check_collision(j1,j2):
    p1,v1,a1=j1[:3],j1[3:6],j1[6:9]
    p2,v2,a2=j2[:3],j2[3:6],j2[6:9]
    dp, dv, da = p1-p2, v1-v2, a1-a2
    # print(dp,dv,da)
    delta=(da/2+dv)**2-2*da*dp
    n1, n2 =np.zeros(3), np.zeros(3)
    for i in range(3):
        if da[i]!=0:
            if delta[i]<=0:
                return 0
            else:
                n1[i] = -0.5-dv[i]/da[i]+np.sqrt(delta[i])/da[i]
                n2[i] = -0.5-dv[i]/da[i]-np.sqrt(delta[i])/da[i]
        elif dv[i]!=0:
            n1[i]=-dp[i]/dv[i]
            n2[i]=n1[i]
        else: 
            return 0
    n1=np.around(n1,4)
    n2=np.around(n2,4)
    n12=np.array([n1,n2]).T
    for n in np.array(np.meshgrid(n12[0],n12[1],n12[2])).T.reshape(-1,3):
        m = np.average(n)
        if np.all(n==m) and m>0:
            return m
    # print(f"We have:\n\t{m1:.2f} (from {n1} so {m1>0} and {n1==m1}),\n\t{m2:.2f} (from {n2} so {m2>0} and {n2==m2})")
    return 0
    
with open("input.dat") as file:
    data = file.read().splitlines()
    
data = np.array([[int(i) for i in list(filter(len,re.split('\n| |=|,|<|>|[a-z]',x)))] for x in data])[:]

print(np.argmin(np.array([np.linalg.norm(j[6:9]) for j in data])))

colliders=[]
for j in range(len(data)):
    for k in range(j+1,len(data)):
        # print(j,k)
        coll=check_collision(data[j],data[k])
        if coll>0:
            colliders.append([coll,j,k])
    if j % (len(data)//50)==0:
        print(j)

print()
colliders.sort(key=lambda x: x[0])
colliders=np.array(colliders)

collision_times=np.unique(colliders[:,0])
collision_times=[[i,list(np.unique(np.ndarray.flatten(colliders[np.where(colliders[:,0]==i)][:,1:])))] for i in collision_times]

# print(colliders)
for i in collision_times:
    print(i)

ct=[k for j in [i[1] for i in collision_times] for k in j]

print(len(ct),len(set(ct)))

print()

for i in range(len(collision_times)):
    for j in range(i):
        collision_times[i][1]=[k for k in collision_times[i][1] if k not in collision_times[j][1]]

ct=[k for j in [i[1] for i in collision_times] for k in j]

print(len(ct),len(set(ct)))