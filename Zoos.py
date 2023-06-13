st=input()
z=0
o=0
for  k in st:
    if k=="z":
        z+=1
    else:
        o+=1
if z*2==o:
    print("Yes")
else:
    print("No")