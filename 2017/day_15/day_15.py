with open("input.dat") as file:
    data = file.readlines()

print(data)

value_A, value_B = 783, 325

factor_A, factor_B = 16807, 48271

# value_A, value_B = 65, 8921

mod_AB=2147483647

count=0

# for i in range(40000000):
#     # print((value_A*factor_A^i-value_B*factor_B^i) % mod_AB % 65536)
#     value_A=(value_A*factor_A)%mod_AB
#     value_B=(value_B*factor_B)%mod_AB
#     if value_A  % 65536==value_B  % 65536:
#         count+=1
        
for i in range(5000000):
    # print((value_A*factor_A^i-value_B*factor_B^i) % mod_AB % 65536)
    value_A=(value_A*factor_A)%mod_AB
    while value_A%4!=0:
        value_A=(value_A*factor_A)%mod_AB
    value_B=(value_B*factor_B)%mod_AB
    while value_B%8!=0:
        value_B=(value_B*factor_B)%mod_AB
    # print(value_A,value_B)
    if value_A  % 65536==value_B  % 65536:
        count+=1
    if i % 500000==0:
        print(i)
        
print(count)

# (a*fa^n-b*fb^n) mod c mod 65536 == 0
