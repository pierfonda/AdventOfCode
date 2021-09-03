import re

with open("input.dat") as file:
    data = file.read().splitlines()

data=data[0]
#data="X(8x2)(3x3)ABCY"
#.data="(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"

def process_string(datas):
    i=0
    decompr=[]
    while i<len(datas):
        if datas[i]!='(':
            decompr.append(datas[i])
        else:
            j=0
            while datas[i+j]!=')':
                j+=1
            char, repeat=[int(x) for x in re.split("x",datas[i+1:i+j])]
            k=0
            while k<repeat:
                decompr.append([x for x in datas[i+j+1:i+j+1+char]])
                k+=1
            i+=j+char
        i+=1
    decompr=[x for y in decompr for x in y]
    print(len(decompr))
    return ''.join(decompr)

def foresee_length(datas):
    i=0
    length=0
    while i<len(datas):
        if datas[i]=='(':
            j=0
            while datas[i+j]!=')':
                j+=1
            char, repeat=[int(x) for x in re.split("x",datas[i+1:i+j])]
            length+=repeat*foresee_length(datas[i+j+1:i+j+1+char])
            i+=j+char
        else:
            length+=1
        i+=1
    
    return(length)

print(foresee_length(data))

#while '(' in data:
#    data=process_string(data)
