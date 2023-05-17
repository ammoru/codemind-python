def num_divi(num):
    digits = str(num)
    for digit in digits:
        if digit == '0' or num % int(digit) != 0:
            return False
    return True
def sef_divi(st,end):
    res1=[]
    for num in range(st,end+1):
        if num_divi(num):
            res1.append(num)
    return res1

n=int(input())
m=int(input())
res=sef_divi(n,m)
for k in res:
    print(k,end=" ")