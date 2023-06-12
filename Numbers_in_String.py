st=input()
l=[]
for k in st:
    if k.isdigit():
        l.append(int(k))
print(sum(l))    