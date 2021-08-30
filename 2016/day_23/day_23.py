with open("input.dat") as file:
    data = file.read().splitlines()
    
#data=["cpy 2 a","tgl a","tgl a","tgl a","cpy 1 a","dec a","dec a"]
    
def execute_command_list_clean(l,registers,c_max):
    sl=[i.split() for i in l]
    c_l=0
    c=0
    while c_l<len(l) and (c<c_max or c_max==0):
        to_read=sl[c_l]
        if to_read[0]=='cpy':
            if (to_read[1].strip('-')).isnumeric():
                registers[to_read[2]]=int(to_read[1])
            else:
                registers[to_read[2]]=registers[to_read[1]]
        elif to_read[0]=='inc':
            registers[to_read[1]]+=1
        elif to_read[0]=='dec':
            registers[to_read[1]]-=1
        elif to_read[0]=='jnz':
            if ((to_read[1].strip('-')).isnumeric() and int(to_read[1])!=0) or (to_read[1] in registers and registers[to_read[1]]!=0):
                if (to_read[2].strip('-')).isnumeric():
                    c_l+=int(to_read[2])-1
                else:
                    c_l+=registers[to_read[2]]-1    
        elif to_read[0]=='tgl':
            t_l=c_l+registers[to_read[1]]
            if t_l<len(sl):
                print(f"At line {t_l+1} changing {sl[t_l]} ->",end='')
                if len(sl[t_l])==2 and sl[t_l][0]=='inc':
                    sl[t_l][0]='dec'
                elif len(sl[t_l])==2:
                    sl[t_l][0]='inc'
                elif len(sl[t_l])==3 and sl[t_l][0]=='jnz':
                    sl[t_l][0]='cpy'
                elif len(sl[t_l])==3:
                    sl[t_l][0]='jnz'
                print(f" {sl[t_l]}'\t\t\tcall from {c},{registers}")
        c_l+=1
        c+=1
    return registers,c  

def execute_command_list(l,registers,c_max):
    sl=[i.split() for i in l]
    c_l=0
    c=0
    while c_l<len(l) and (c<c_max or c_max==0):
        to_read=sl[c_l]
#        print(f"Reading line {c_l+1} with value {' '.join(to_read)} {registers} {c}")
        if c_l==4:
            c+=((3*registers['b']-1)+4)*registers['d']-1
            registers['a']= registers['d']*registers['b']
            registers['d']= 0
            registers['c']= 0
            c_l=9
        elif c_l<len(l)-2 and sl[c_l][0]=='inc' and sl[c_l+1][0]=='dec' and sl[c_l+2][0]=='jnz':
            registers[sl[c_l][1]]+=registers[sl[c_l+1][1]]
            c+=3*registers[sl[c_l+1][1]]-2
            registers[sl[c_l+1][1]]=0
            c_l+=1
        elif to_read[0]=='cpy':
            if (to_read[1].strip('-')).isnumeric():
                registers[to_read[2]]=int(to_read[1])
            else:
                registers[to_read[2]]=registers[to_read[1]]
        elif to_read[0]=='inc':
            registers[to_read[1]]+=1
        elif to_read[0]=='dec':
            registers[to_read[1]]-=1
        elif to_read[0]=='jnz':
            if ((to_read[1].strip('-')).isnumeric() and int(to_read[1])!=0) or (to_read[1] in registers and registers[to_read[1]]!=0):
                if (to_read[2].strip('-')).isnumeric():
                    c_l+=int(to_read[2])-1
                else:
                    c_l+=registers[to_read[2]]-1    
        elif to_read[0]=='tgl':
            t_l=c_l+registers[to_read[1]]
            if t_l<len(sl):
                print(f"At line {t_l+1} changing {sl[t_l]} ->",end='')
                if len(sl[t_l])==2 and sl[t_l][0]=='inc':
                    sl[t_l][0]='dec'
                elif len(sl[t_l])==2:
                    sl[t_l][0]='inc'
                elif len(sl[t_l])==3 and sl[t_l][0]=='jnz':
                    sl[t_l][0]='cpy'
                elif len(sl[t_l])==3:
                    sl[t_l][0]='jnz'
                print(f" {sl[t_l]}'\t\t\tcall from {c},{registers}")
#        print(registers)
        c_l+=1
        c+=1
    return registers,c
#    print("Value of registers after operation:",registers,"\n")
    
    
CCMAX=0
print(execute_command_list(data,{'a':12},CCMAX))
#print(execute_command_list_clean(data,{'a':12},CCMAX))