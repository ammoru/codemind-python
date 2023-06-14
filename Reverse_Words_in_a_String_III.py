st=input().split( )
ls=[]
for i in st:
    ls.append(i[::-1])
for k in ls:
    print(k,end=" ")