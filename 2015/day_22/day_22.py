from itertools import product 

with open("input.dat") as file:
    data = file.read()

# Structure of a player: [name, HP, damage, base_shield, shield, mana,[bufferlist]]
# Structure of a spell: [mana cost, instant vs effect, damage, heal, shield increase, recharge, turns]

spells={
        "Magic Missile":[53,"Instant",4,0,0,0,0],
        "Drain":[73,"Instant",2,2,0,0,0],
        "Shield":[113,"Defense Effect",0,0,7,0,6],
        "Poison":[173,"Attack Effect",3,0,0,0,6],
        "Recharge":[229,"Defense Effect",0,0,0,101,5]
        }

leneff=0
effect_position={}

for i in spells:
    if "Effect" in spells[i][1]:
        effect_position[i]=leneff
        leneff+=1        

position_effects={v: k for k, v in effect_position.items()}

def playerstat(plyr,nl=""):
    print(plyr[0]+" has",plyr[1],"HP,",plyr[2],"damage,",plyr[4],"shield,",plyr[5],"mana."+nl)
   
def cast_spell(spell,player_from,player_to):
    try:   
        spl=spells[spell]
    except KeyError:
        print("\""+spell+"\" is not a valid spell!\n")
        return None
    if player_from[5]-spl[0]<0:
#        print("Not enough mana to cast "+spell+"!")
        return None
#    print(player_from[0]+" cast "+spell+"!")
    if spl[1]=="Instant":
        player_to[1]-=spl[2]
        player_from[1]+=spl[3]
        player_from[5]-=spl[0]
        return 1
    elif spl[1]=="Defense Effect":
        effpos=effect_position[spell]
        if player_from[-1][effpos]==0:
            player_from[-1][effpos]=spl[-1]
            player_from[5]-=spl[0]
            return 1
    elif spl[1]=="Attack Effect":
        effpos=effect_position[spell]
        if player_to[-1][effpos]==0:
            player_to[-1][effpos]=spl[-1]
            player_from[5]-=spl[0]
            return 1
    return None

def normal_attack(player_from,player_to):
    player_to[1]-=max(1,player_from[2]-player_to[4])
#    print(player_from[0],"attacks",player_to[0],"with normal weapons!")

def check_buffs(plyr):
    buffs=plyr[-1]
    plyr[4]=plyr[3]
    for i in range(leneff):
        if buffs[i]>0:
            spl=spells[position_effects[i]]
            plyr[1]-=spl[2]
            plyr[4]+=spl[4]
            plyr[5]+=spl[5]
            buffs[i]-=1
#            print("The buff",position_effects[i],"has effect on",plyr[0],"(valid for",buffs[i],"more turns)")
            
def one_turn(player_1,player_2,n,lose=False):
#    playerstat(player_1)
#    playerstat(player_2)
    if lose:
        player[1]-=1
    check_buffs(player_1)        
    check_buffs(player_2)
    if player_1[1]<=0 or player_2[1]<=0:
        return 0
    if n in range(len(list(spells.keys()))):
        casted=cast_spell(list(spells.keys())[n],player_1,player_2)
        if casted==1:
            return spells[list(spells.keys())[n]][0]
    else:
        normal_attack(player_1,player_2)
    return 0

def fight(player_1,player_2,sequence):
    nturns=0
    mana_spent=0
    i=0
    while player_1[1]>0 and player_2[1]>0:
        if len(sequence)>i:
            mana_spent+=one_turn(player_1,player_2,sequence[i],False)
            i+=1
        else: 
            mana_spent+=one_turn(player_1,player_2,sequence[-1],False)
        nturns+=1
        if player_1[1]<=0:
            return [nturns,0,mana_spent]
        if player_2[1]<=0:
            return [nturns,1,mana_spent]
        one_turn(player_2,player_1,-1)
        nturns+=1
        if player_1[1]<=0:
            return [nturns,0,mana_spent]
        if player_2[1]<=0:
            return [nturns,1,mana_spent]     

boss=["Boss",int(data.split()[2]),int(data.split()[4]),0,0,0,[0]*leneff]
player=["Terzeni",50,0,0,0,500,[0]*leneff]

boss=["Boss",13,8,0,0,0,[0]*leneff]
player=["Terzeni",10,0,0,0,250,[0]*leneff]

win_list=[]
for i in product(range(5),repeat=2):
    j=list(i)
    boss=["Boss",13,8,0,0,0,[0]*leneff]
    player=["Terzeni",10,0,0,0,250,[0]*leneff]    
    fought=fight(player,boss,j)
#    if fought!=None and fought[1]==0: 
#        print(player[0], "has lost after spending",fought[2],"mana and",fought[0],"turns and sequence",j,"!")
    if fought!=None and fought[1]==1:  
        print(player[0], "has won after spending",fought[2],"mana and",fought[0],"turns and sequence",j,"!")
        win_list.append(int(fought[2]))

print(min(win_list))
print(len(win_list))
print(sorted(set(win_list)))
        