n=int(input())
res=list(map(int,input().split()))
a,b=map(int,input().split())
l=[]
fa=0
for  i in res:
    if i<a or i>b:
        l.append(i)
        fa=1
if fa==1:
    print(min(l))
else:
    print('-1')