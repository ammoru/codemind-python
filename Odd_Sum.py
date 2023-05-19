n=int(input())
k=list(map(int,input().split()))
su=0
for i in k:
    if i%2!=0:
        su+=i
print(su)        