with open("input.dat") as file:
    data = file.read().strip()

# part 1
tot=0
for i in range(len(data)):
    nxt= (i+1) % len(data)
    if data[i]==data[nxt]:
        tot+=int(data[i])

print(tot)

# part 2
tot=0
for i in range(len(data)):
    nxt= (i+(len(data)//2)) % len(data)
    if data[i]==data[nxt]:
        tot+=int(data[i])

print(tot)