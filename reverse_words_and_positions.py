lis= list(map(str,input().split()))
ls2=[]
for i in lis:
    ls2.append(i[::-1])
print(*ls2[::-1])    