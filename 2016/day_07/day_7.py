with open("input.dat") as file:
    data = file.read().splitlines()
    
found=0
    
for i in range(len(data)):
    hasabba=0
    check_parenthesis=0
    for j in range(len(data[i])-3):
        if data[i][j]=='[':
            check_parenthesis+=1
        elif data[i][j]==']':
            check_parenthesis-=1          
        elif data[i][j]==data[i][j+3] and data[i][j+1]==data[i][j+2] and data[i][j]!=data[i][j+1] and check_parenthesis==0:
            hasabba+=1
        elif data[i][j]==data[i][j+3] and data[i][j+1]==data[i][j+2] and data[i][j]!=data[i][j+1] and check_parenthesis>0:
            hasabba-=1
    if hasabba>0:
        found+=1

print(found)

found=0
    
for i in range(len(data)):
    abalist=[]
    nabalist=[]
    check_parenthesis=0
    for j in range(len(data[i])-2):
        if data[i][j]=='[':
            check_parenthesis+=1
        elif data[i][j]==']':
            check_parenthesis-=1          
        elif data[i][j]==data[i][j+2] and data[i][j]!=data[i][j+1] and check_parenthesis==0:
            abalist.append(list(data[i][j:j+2]))
        elif data[i][j]==data[i][j+2] and data[i][j]!=data[i][j+1] and check_parenthesis>0:
            nabalist.append([data[i][j+1],data[i][j]])
    for a in abalist:
        for b in nabalist:
            if a==b:
                found+=1
#                print("\t",abalist,"\n\t",nabalist,"\n")
                break
        else:
            continue
        break

print(found)