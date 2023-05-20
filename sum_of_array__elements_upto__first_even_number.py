n=int(input())
k=list(map(int,input().split()))
su=0
for i in range(len(k)):
    
    if k[i]%2==0:
        break
    su+=k[i]
print(su)        