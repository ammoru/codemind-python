def fun(v):
    su=0
    for i in range(1,v):
        if v%i==0:
            su+=i
    return su

n=int(input())
sur=fun(n)
if sur>n:
    print(True)
else:
    print(False)