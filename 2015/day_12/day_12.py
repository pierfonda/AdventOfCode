import json

with open("input.dat") as file:
    data=json.load(file)

def print_int(jsondict):
    global tot
    skip=False
    if isinstance(jsondict, dict):
        for i in jsondict:
            if jsondict[i]=="red":
                skip=True
        for i in jsondict:
            if isinstance(jsondict[i], int) and not skip:
                tot+=jsondict[i]
            elif not skip:
                print_int(jsondict[i])
    elif isinstance(jsondict, list):
        for i in jsondict:
            if isinstance(i, int):
                tot+=i
            else:
                print_int(i)
    elif isinstance(jsondict, str):
        None
             
tot=0
print_int(data)

print("Total sum:",tot)