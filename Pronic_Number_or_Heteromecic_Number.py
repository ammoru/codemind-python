n=int(input())
a=0
b=1
l=0
for i in range(n):
    if a*b==n:
        l+=1
        break
    else:
        b+=1
        a+=1
if l!=0:
    print("YES")
else:
    print("NO")