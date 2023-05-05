n=int(input())
for i in range(n):
    for k in range(1,n+1-i):
        print(k,end="")
    print()    