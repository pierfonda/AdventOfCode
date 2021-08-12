import string

llc=list(string.ascii_lowercase)

def increment_str(in_str):
    out_str=list(in_str)
    for i in out_str:
        if i not in llc:
            print("Not a lowercase string!")
            return None
            exit
    for i in range(len(out_str)):
        if out_str[-i-1]!="z":
            out_str[-i-1]=llc[llc.index(out_str[-i-1])+1]
            return "".join(out_str)
            exit
        else:
            out_str[-i-1]="a"    
    for i in range(len(out_str)):
        out_str[i]="a"
    return "".join(out_str)

def check_sequence(in_str):
    if len(in_str)<3:
        print("String too short!")
        return None
        exit
    for i in in_str:
        if i not in llc:
            print("Not a lowercase string!")
            return None
            exit
    for i in range(len(in_str)-2):
        if in_str[i]!="y" and in_str[i]!="z" and in_str[i+1]==llc[llc.index(in_str[i])+1] and in_str[i+2]==llc[llc.index(in_str[i])+2]:
            return True
            exit
    return False

def check_intruder(in_str):
    for i in in_str:
        if i=="o" or i=="o" or i=="l":
            return False
            exit
    return True

def check_double(in_str):
    count_double=0
    i=0
    while i < len(in_str)-1:
        if in_str[i+1]==in_str[i]:
            count_double+=1
            if i<len(in_str)-2:
                if in_str[i+2]==in_str[i]:
                    i+=1
        i+=1
    if count_double>1:
        return True
    else:
        return False

data_string="cqjxjnds"

finish=False
while not finish:
    if check_sequence(data_string) and check_intruder(data_string) and check_double(data_string):
        finish=True
        print("Finished! Final string:",data_string)
    data_string=increment_str(data_string)

finish=False
while not finish:
    if check_sequence(data_string) and check_intruder(data_string) and check_double(data_string):
        finish=True
        print("Finished! Final string for part 2:",data_string)
    data_string=increment_str(data_string)
