n=int(input())
k=list(map(int,input().split()))
su,su1=0,0
for o in range(len(k)):
    if k[o]%2==0:
        su+=k[o]
    else:
        su1+=k[o]
print(abs(su-su1))      