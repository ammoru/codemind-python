n=input()
x=1
su=0
for i in range(len(n)):
    j=int(n[i])**x
    su=su+j
    x+=1
if str(su)==n:
    print(True)
else:
    print(False)
    