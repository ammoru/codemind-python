n=int(input())
res= list(map(int,input().split()))
a,b=map(int,input().split())
s=0
flag=0
for i in res:
    if i<a or i>b:
        flag=1
        print(i,end=" ")
if flag==0:
    print("-1")
    