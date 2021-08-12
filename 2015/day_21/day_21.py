import itertools 

with open("input.dat") as file:
    boss = file.read()
boss=[int(boss.split()[2]),int(boss.split()[4]),int(boss.split()[6])]
me=[100,0,0]

with open("shop.dat") as file:
    shop = file.readlines()
shop = [x.strip() for x in shop]

  
weapons=[]
armors=[[0,0,0]]
rings=[[0,0,0],[0,0,0]]  
for i in range(6):
    if i<5:
        tmp=shop[i+1].split()
        weapons.append([int(tmp[1]),int(tmp[2]),int(tmp[3])])
        tmp=shop[i+8].split()
        armors.append([int(tmp[1]),int(tmp[2]),int(tmp[3])])
        tmp=shop[i+15].split()
        rings.append([int(tmp[-3]),int(tmp[-2]),int(tmp[-1])])
    else:
        tmp=shop[i+15].split()
        rings.append([int(tmp[-3]),int(tmp[-2]),int(tmp[-1])])

def fight(p1,p2):
    hp1=p1[0]
    hp2=p2[0]
    while hp1>0 or hp2>0:
        hp2-=max(1,(p1[1]-p2[2]))
        if hp2<=0:
            return 1
        hp1-=max(1,(p2[1]-p1[2]))
        if hp1<=0:
            return 0

win_money=[]
lose_money=[]
for i in weapons:
    for j in armors:
        for k,l in itertools.combinations(rings, 2):
            t_me=[100,0,0]
            t_me[1]+=i[1]+k[1]+l[1]
            t_me[2]+=j[2]+k[2]+l[2]
   #         print(t_me,boss,i[0]+j[0]+k[0]+l[0])
            if fight(t_me,boss):
                win_money.append(i[0]+j[0]+k[0]+l[0])
            else:
                lose_money.append(i[0]+j[0]+k[0]+l[0])
                
print(sorted(win_money)[0])
print(sorted(lose_money)[-1])