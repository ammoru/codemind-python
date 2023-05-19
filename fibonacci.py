n=int(input())
a,b=0,1
print(0,1,end=" ")
for i in range(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    
    