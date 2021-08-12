import hashlib

puzzle_input="ahsbgdzn"
#puzzle_input="abc"

keys=[]
otp_found=0
otp_max=64
t_max=1
i=0

def get_hash(string,n):
    tmphas=(hashlib.md5(string.encode())).hexdigest()
    for j in range(n):
        tmphas=(hashlib.md5(tmphas.encode())).hexdigest()
    return tmphas


while otp_found<otp_max:
    i+=1
#    hexmd5i=(hashlib.md5((puzzle_input+str(i)).encode())).hexdigest()
    hexmd5i=get_hash(puzzle_input+str(i),2016)
    t_cur=0
    for j in range(len(hexmd5i)-2):
        if hexmd5i[j:j+3]==3*hexmd5i[j] and t_cur<t_max:
            t_cur+=1
            t_isgood=False
            for k in range(1000):
#                hexmd5k=(hashlib.md5((puzzle_input+str(i+k+1)).encode())).hexdigest()
                hexmd5k=get_hash(puzzle_input+str(i+k+1),2016)
                for l in range(len(hexmd5i)-4):
                    if hexmd5k[l:l+5]==5*hexmd5i[j] and not t_isgood:
                        if i not in keys:
                            keys.append(i)
                            otp_found+=1
                            t_isgood=True
                            print(f"Key {i} contains {hexmd5i[j:j+3]} and Key {i+k+1} contains {hexmd5k[l:l+5]}")
                if t_isgood:
                    break

print(keys)
print(len(keys))
