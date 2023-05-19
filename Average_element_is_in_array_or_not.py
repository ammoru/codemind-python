n=int(input())
k=list(map(int,input().split()))
l=sum(k)//n
if l in k:
    print(True)
else:
    print(False)