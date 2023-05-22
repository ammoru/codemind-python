n=int(input())
res= list(map(int,input().split()))
a,b=map(int,input().split())
s=0
for i in res:
    if i>=a and i<=b:
        s+=i
print(sum(res)-s)    