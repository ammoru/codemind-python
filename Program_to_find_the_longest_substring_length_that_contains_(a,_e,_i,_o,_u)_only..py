st=input()
cn=0
maxx=0
for k in st:
    if k in "AEIOUaeiou":
        cn+=1
        maxx=max(maxx,cn)
    else:
        cn=0
print(maxx)        