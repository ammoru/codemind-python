def fun(num):
    s=0
    for i in range(1,num+1):
        if num%i == 0:
            s=s+i
    return s
n=int(input())
m=int(input())
if fun(n)==fun(m):
    print("Amicable")
else:
    print('Not Amicable')
