x,y=map(int,input().split())
k=2*y
l=x+k
if (x == 0 and y % 2 == 0):
    print("YES")
elif (x == 0 and y % 2 != 0):
    print("NO")
elif ((x + (2 * y)) % 2 == 0):
    print("YES")
else:
    print("NO")