import hashlib

inputStr="ffykfhsq"

#inputStr="abc"

i=0
password=''

#while len(password)<8:
#    i+=1
#    var=hashlib.md5((inputStr+str(i)).encode('utf-8')).hexdigest()
#    if var[:5]=='00000' :
##        print("at",i,"the md5 hash is",var)
#        password+=var[5]
#        print(var[5],end="")

i=0
#inputStr="abc"
inputStr="ffykfhsq"
password=["_"] * 8
found=0

while found<len(password):
    i+=1
    var=hashlib.md5((inputStr+str(i)).encode('utf-8')).hexdigest()
    if var[:5]=='00000' :
        if var[5].isnumeric() and int(var[5])<len(password) and password[int(var[5])]=='_':
            password[int(var[5])]=var[6]
            found+=1
            print(password)
            
print("".join(password))