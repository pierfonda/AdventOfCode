import re

with open("input.dat") as file:
    data = file.readlines()

data = [re.split(' |, |\n',x) for x in data]   

exit_loop=False
cur_index=0
registers={"a":1,"b":0}

while not exit_loop:
    if cur_index<len(data):
        instr=data[cur_index]
        if instr[0]=="hlf":
            registers[instr[1]]=registers[instr[1]]/2
            cur_index+=1
        elif instr[0]=="tpl":
            registers[instr[1]]=3*registers[instr[1]]
            cur_index+=1            
        elif instr[0]=="inc":
            registers[instr[1]]+=1
            cur_index+=1 
        elif instr[0]=="jmp":
            cur_index+=int(instr[1])
        elif instr[0]=="jie":
            if registers[instr[1]]%2==0:
                cur_index+=int(instr[2])
            else:
                cur_index+=1 
        elif instr[0]=="jio":
            if registers[instr[1]]==1:
                cur_index+=int(instr[2])
            else:
                cur_index+=1 
    else:
        exit_loop=True
        
print("The b register has value",registers["b"])