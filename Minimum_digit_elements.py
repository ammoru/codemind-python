n=int(input())
lst=list(map(int,input().split()))
k=[]
cn=0
for ka in lst:
    #print(ka)
    k.append(len(str(ka)))
for sa in lst:
    if min(k)==len(str(sa)):
        cn+=1
print(cn)        