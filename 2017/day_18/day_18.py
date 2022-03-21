import re

def getint(var,reg):
    return int(var) if var.strip('-').isnumeric() else reg[var]

def execute_instruction(to_read, reg, index, send, receive):
    exitloop=False
    if to_read[1] not in reg and not to_read[1].strip('-').isnumeric():
        reg[to_read[1]]=0
    if to_read[0]=='snd':
        send.append(getint(to_read[1],reg))
        # print(f"Sending out {send}")
    elif to_read[0]=='set':
        reg[to_read[1]]=getint(to_read[2],reg)
        # print(f"Setting register {to_read[1]} to {registers[to_read[1]]}")
    elif to_read[0]=='add':
        reg[to_read[1]]+=getint(to_read[2],reg)
        # print(f"Increasing register {to_read[1]} to {registers[to_read[1]]}")
    elif to_read[0]=='mul':
        reg[to_read[1]]*=getint(to_read[2],reg)
        # print(f"Multiplying register {to_read[1]} with {to_read[2]} to {registers[to_read[1]]}")
    elif to_read[0]=='mod':
        reg[to_read[1]]=reg[to_read[1]] % getint(to_read[2],reg)
        # print(f"Modding register {to_read[1]} with {to_read[2]} to {registers[to_read[1]]}")
    elif to_read[0]=='jgz':
        if getint(to_read[1],reg)>0:
            index+=getint(to_read[2],reg)-1
        # print(f"Jumping to {cur_index}")
    elif to_read[0]=='rcv':
        if getint(to_read[1],reg)>0:
            receive.append(getint(to_read[1],reg))
            print(f"Receiving {receive} (last sent:{send[-1]})")
            exitloop=True
    return reg, index+1, exitloop, send, receive

def execute_instruction2(to_read, reg, index, send, other_send, switch_ID, sendcall):
    switch_ID=False
    exitloop=False
    if to_read[1] not in reg and not to_read[1].strip('-').isnumeric():
        reg[to_read[1]]=0
    if to_read[0]=='snd':
        send.append(getint(to_read[1],reg))
        sendcall+=1
        # print(f"Function 'snd' called with {to_read}, {reg}, {index}, {send}, {other_send}, {switch_ID}")
    elif to_read[0]=='set':
        reg[to_read[1]]=getint(to_read[2],reg)
    elif to_read[0]=='add':
        reg[to_read[1]]+=getint(to_read[2],reg)
    elif to_read[0]=='mul':
        reg[to_read[1]]*=getint(to_read[2],reg)
    elif to_read[0]=='mod':
        reg[to_read[1]]=reg[to_read[1]] % getint(to_read[2],reg)
    elif to_read[0]=='jgz':
        if getint(to_read[1],reg)>0:
            index+=getint(to_read[2],reg)-1
    elif to_read[0]=='rcv':
        if len(other_send)>0:
            reg[to_read[1]]=other_send[0]
            other_send=other_send[1:]
            switch_ID=True
        else:
            exitloop=True
            switch_ID=True
            index-=1
        # print(f"Function 'rcv' called with {to_read}, {reg}, {index}, Send length: {len(send)}, Receive length: {len(other_send)}, {switch_ID}, {exitloop}")
    return reg, index+1, send, other_send, switch_ID, exitloop, sendcall
    
with open("input.dat") as file:
    data = file.readlines()

data = [re.split(' |, |\n',x) for x in data]   

exit_loop=False
send, receive=[],[]
cur_index=0
registers={}

while not exit_loop:
    if -1<cur_index<len(data):
        instruction=data[cur_index][:-1] 
        registers, cur_index, exit_loop, send, receive = execute_instruction(instruction, registers, cur_index, send, receive)
    else:
        exit_loop=True
        
print()

# with open("example_2.dat") as file:
#     data = file.readlines()

# data = [re.split(' |, |\n',x) for x in data] 
    
ex = [False, False]
reg=[{'p':0},{'p':1}]
send=[[],[]]
calls=[0,0]
sendcalls=[0,0]
cur_index = [0,0]
i=0

while not (ex[0] and ex[1]) and -1<cur_index[0]<len(data) and -1<cur_index[1]<len(data):
    switch_ID=False
    instruction=data[cur_index[i]][:-1]
    reg[i], cur_index[i], send[i], send[(i+1)%2], switch_ID, ex[i], sendcalls[i] = execute_instruction2(instruction, reg[i], cur_index[i], send[i], send[(i+1)%2], switch_ID, sendcalls[i])
    calls[i]+=1
    if switch_ID:
        i=(i+1)%2
        switch_ID=False

print(ex,reg,cur_index,[len(j) for j in send],calls)
print(sendcalls)
        
