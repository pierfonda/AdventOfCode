with open("input.dat") as file:
    data = file.read()

# print(data)

# data='{{{},{},{{}}}} '

score=0
garbage_score=0
garbage=False
ignore=False
groups=0
unclosed_groups=0
for i in range(len(data)):
    if ignore:
        ignore=False
        pass
    elif data[i]=='!':
        ignore=True
    elif data[i]=='<' and not garbage:
        garbage=True
    elif data[i]=='>' and garbage:
        garbage=False
    elif data[i]=='{' and not garbage:
        unclosed_groups+=1
    elif data[i]=='}' and not garbage:
        unclosed_groups-=1
        score+=(1+unclosed_groups)
    elif garbage:
        garbage_score+=1
    # print(f"{i} {ignore} {data[i]} {garbage} {groups} {unclosed_groups}")
        
print(score)
print(garbage_score)
    
