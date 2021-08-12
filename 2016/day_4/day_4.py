import re

with open("input.dat") as file:
    data = file.readlines()
    
class circ(list):
    def __getitem__(self, idx):
        return super(circ, self).__getitem__(idx % len(self))

data = [re.split('\n|-|\[|\]',x) for x in data]

def compute_room_hash(line):
    freq={}
    for i in range(len(line)-4):
        for j in line[i]:
            if j in freq:
                freq[j]+=1
            else:
                freq[j]=1
    freq={k: v for k, v in sorted(freq.items(), key=lambda x: (-x[1],x[0]))}
    hash=''
    for j in list(freq.keys())[0:5]:
        hash+=j
    return(hash)
    
def check_room_hash(line):
    if compute_room_hash(line)==line[-3]:
        return(int(line[-4]))
    else:
        return(0)

alphabet=circ(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"])


def shift_letter(letter,n):
    return(alphabet[alphabet.index(letter)+n])
    
print(tot)


tot=0
for q in data:
    tot+=check_room_hash(q)
    for j in q[:-4]:
        word=''
        for i in j:
            word+=shift_letter(i,int(q[-4]))
        if 'ole' in word:
            print(word,"",end = '')
            print(q)
    
