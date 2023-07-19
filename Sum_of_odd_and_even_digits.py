num=int(input())
lst=list(map(int,input().split()))
su=0
su1=0
for i  in range(num):
        if i%2==0:
            su1+=lst[i]
        else:
            su+=lst[i]
if (su-su1):
    print("NO")
else:
    print("YES")
    
    