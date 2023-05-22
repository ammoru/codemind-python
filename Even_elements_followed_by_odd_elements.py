n=int(input())
res=list(map(int,input().split()))
for  i in range(n):
    if res[i]%2==0:
        print(res[i],end=" ")
for  k in range(n):
    if res[k]%2!=0:
        print(res[k],end=" ")        