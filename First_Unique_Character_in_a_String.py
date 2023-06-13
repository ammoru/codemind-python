t=input().strip()
cn=0
ls=[]
for k in t:
    if k not in ls and t.count(k)==1:
        ls.append(k)
if len(ls)==0:
    print('-1')
else:    
    print(t.index(ls[0]))
