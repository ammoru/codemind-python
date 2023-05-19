def fun(num):
    c=0
    for i in range(1,n+1):
        if num%i==0:
            c+=1
    return c        

n=int(input())
cn=fun(n)
if cn==2:
    print("prime")
else:
    print("not a prime")