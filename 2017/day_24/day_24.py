with open("input.dat") as f:
  data = sorted([list(map(int, line.split("/"))) for line in f])

starts=[i for i in data if i[0]==0 or i[1]==0]

print()

def links(start,pool,spos=0):
    yield (start,)
    p=[i for i in pool if i!=start]
    opos=(spos+1)%2
    available=[j for j in p if start[opos] in j]
    for k in available:
        npos=0 if k[0]==start[opos] else 1
        for n in links(k,p,npos):
            yield (start,)+n

print()
max_score=0
max_length=0
max_lengthscore=0
n=0

for j in starts:
    for i in links(j,data):
        score=sum(a+b for a,b in i)
        length=len(i)
        if score>max_score:
            max_score=score
            max_sequence=i
            # print(i)
        if length>=max_length and score>max_lengthscore:
            max_length=length
            max_lengthscore=score
            max_lengthsequence=i
            
print(max_score,max_sequence)

print()

print(max_length,max_lengthscore,max_lengthsequence)

