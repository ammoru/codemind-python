n=int(input())
k=list(map(int,input().split()))
k1=k[::-1]
for i in k1:
    if i%2==0:
        print(i)
        break;
