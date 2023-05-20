n=input()
po=1
su=0
for i in n:
    su+=int(i)
    po*=int(i)
print(abs(su-po))    
    
