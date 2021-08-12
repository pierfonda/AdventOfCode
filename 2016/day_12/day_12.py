with open("input.dat") as file:
    data = file.read().splitlines()
    
#data=["cpy 41 a","inc a","inc a","dec a","jnz a 2","dec a"]

current_line=0
safecount=0
registers={}
registers['c']=1

while current_line<len(data):
    to_read=data[current_line].split()
#    print("Value of registers before operation:",registers)
#    print(f"Reading line {current_line+1} with value {to_read}")
    if to_read[0]=='cpy':
        if to_read[1].isnumeric():
            registers[to_read[2]]=int(to_read[1])
        else:
            registers[to_read[2]]=registers[to_read[1]]
    elif to_read[0]=='inc':
        registers[to_read[1]]+=1
    elif to_read[0]=='dec':
        registers[to_read[1]]-=1
    elif to_read[0]=='jnz':
        if (to_read[1].isnumeric() and int(to_read[1])!=0) or (to_read[1] in registers and registers[to_read[1]]!=0):
            current_line+=int(to_read[2])-1
    current_line+=1
    safecount+=1
#    print("Value of registers after operation:",registers,"\n")
#    print("Value of registers after operation:",registers,"\n")

print(registers,safecount)
