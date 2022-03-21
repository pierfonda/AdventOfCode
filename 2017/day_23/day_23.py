import re,sys
import math

def getint(var,reg):
    return int(var) if var.strip('-').isnumeric() else reg[var]

def execute_instruction(to_read, reg, index):
    mulcalled=False
    if to_read[1] not in reg and not to_read[1].strip('-').isnumeric():
        reg[to_read[1]]=0
    if to_read[0]=='set':
        reg[to_read[1]]=getint(to_read[2],reg)
        # print(f"Setting register {to_read[1]} to {registers[to_read[1]]}")
    elif to_read[0]=='add':
        reg[to_read[1]]+=getint(to_read[2],reg)
        # print(f"Increasing register {to_read[1]} to {registers[to_read[1]]}")
    elif to_read[0]=='sub':
        reg[to_read[1]]-=getint(to_read[2],reg)
        # print(f"Decreasing register {to_read[1]} to {registers[to_read[1]]}")
    elif to_read[0]=='mul':
        reg[to_read[1]]*=getint(to_read[2],reg)
        mulcalled=True
        # print(f"Multiplying register {to_read[1]} with {to_read[2]} to {registers[to_read[1]]}")
    elif to_read[0]=='jnz':
        if getint(to_read[1],reg)!=0:
            index+=getint(to_read[2],reg)-1
            # print(f"Jumping to {index+1} (registers: {reg})")
    else:
        print("Error! Instruction not recognized!")
        sys.exit
    return reg, index+1, mulcalled
    
with open("input.dat") as file:
    data = file.readlines()

data = [re.split(' |, |\n',x) for x in data]   

exit_loop=False
cur_index=0
registers={'a':1}
m=0
i=0

while not exit_loop and i<1250:
    if -1<cur_index<len(data):
        if cur_index==16:
            print(f"{i}\t{cur_index}\t{data[cur_index][:-1] }\t{m}\t{registers}")
        # if cur_index==19:
        #     m+=1
        #     i+=9
        #     registers['e']+=1
        #     registers['g']+=1
        #     cur_index=11
        instruction=data[cur_index][:-1] 
        registers, cur_index, mul_called = execute_instruction(instruction, registers, cur_index)
        if mul_called:
            m+=1
    else:
        exit_loop=True
    i+=1
        
print()
print(m,registers)

h = 0
for x in range(109900,126900 + 1,17):
	for i in range(2,math.floor(math.sqrt(x)+1)):
		if x % i == 0:
			h += 1
			break
print(h)

