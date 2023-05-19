n=int(input())
x,y=0,1
c=0
for i in range(n+1):
    if x*y==n:
        c+=1
        break
    else:  
        x+=1
        y+=1
if c==1:
    print("YES")
else:
    print("NO")
        
    