import time

my_input='01110110101001000'
disk_size=272
disk_size=35651584

def rev_not(s):
    q=''
    for j in s:
        if j=='0' or j=='1':
            q=str(1-int(j))+q
        else:
            q=j+q
    return(q) 

def fill_disk(s):
    return(s+'0'+rev_not(s))
    
def get_char(s,n):
    q=s
    while len(q)<n:
        q=fill_disk(q)
    return q[n-1]

def get_zero(n):
    if n % 4 == 1:
        return 0
    elif n % 4 == 3:
        return 1
    elif n>0:
        return get_zero(int(n/2))

def get_filled_disk(s,ds):
    n=1
    q=''
    while len(q)<ds:
        q+=s
        q+=str(get_zero(n))
        q+=rev_not(s)
        q+=str(get_zero(n+1))
        n+=2
    return q[:ds]
    
def checksum(s):
    q=''
    for i in range(0,len(s)-1,2):
        if s[i]==s[i+1]:
            q+='1'
        else:
            q+='0'
    if len(q)>1 and len(q) % 2 == 0:
        q = checksum(q)
    return(q)
    

start = time.time()   
s=get_filled_disk(my_input,disk_size)
end = time.time()
t2=end-start

print(t2)

print(checksum(s))