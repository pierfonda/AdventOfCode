start=20151125

def next_code(number):
    return((number*252533)%33554393)
    
n=1
x=1
y=1

while x!=3075 or y!=2981:
    if y==1:
        if x==1:
            y=2;
        else:
            y=x+1;
            x=1;
    else:
        y-=1;
        x+=1;
    n+=1

print(x,y,n)

for j in range(n-1):
    start=next_code(start)

print(start)