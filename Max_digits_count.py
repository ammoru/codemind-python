n=int(input())
lst=list(map(int,input().split()))
k=[len(str(i)) for i in lst]
cn=0
for v in lst:
    if max(k)==len(str(v)):
        cn+=1
print(cn)        