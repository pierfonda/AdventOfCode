with open("input.dat") as file:
    data = file.read().splitlines()

numberofbots=set()
numberofoutputs=set()

for d in data:
    ld=d.split()
    for j in range(len(ld)):
        if ld[j]=='bot':
            numberofbots.add(int(ld[j+1]))
        elif ld[j]=='output':
            numberofoutputs.add(int(ld[j+1]))
            
botstatus= {j:set() for j in numberofbots}
outputstatus= {j:set() for j in numberofoutputs}

for d in data:
    ld=d.split()
    if ld[0]=='value':
        botstatus[int(ld[-1])].add(int(ld[1]))

changes=1
while changes>0:
    changes=0
    for d in data:
        ld=d.split()
        if ld[0]=='bot':
            cb=int(ld[1])
            cm=int(ld[6])
            cM=int(ld[11])
            if len(botstatus[cb])==2:
                if min(botstatus[cb])==17 and max(botstatus[cb])==61:
                    print(cb,botstatus[cb])
                changes+=1
                if ld[5]=='bot':
                    botstatus[cm].add(min(botstatus[cb]))
                elif ld[5]=='output':
                    outputstatus[cm].add(min(botstatus[cb]))
                if ld[10]=='bot':
                    botstatus[cM].add(max(botstatus[cb]))
                elif ld[10]=='output':
                    outputstatus[cM].add(max(botstatus[cb]))
                botstatus[cb]=set()
            
for i in range(len(botstatus)):
    if len(botstatus[i])>0:
        print("Bot",i,"has values:",list(botstatus[i]))     
        
for i in range(len(outputstatus)):
    if len(outputstatus[i])>0:
        print("Output",i,"has values:",list(outputstatus[i]))  
        
print(max(outputstatus[0])*max(outputstatus[1])*max(outputstatus[2]))