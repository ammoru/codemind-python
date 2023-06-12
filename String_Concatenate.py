st1=input()
st2=input()
re=""
st3=st1.strip()+st2.strip()
k=sorted(st3)
for l in k:
    re+=l
print(re)    