n=input()
d={}
c=0
for i  in n:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for k in d.values():
    if k!=1:
        c+=1
        break
if c!=1:
    print("Unique Number")
else:
    print("Not Unique Number")
