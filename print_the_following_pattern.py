st=" ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n=int(input())
for i in range(n,0,-1):
    for k in range(1,i+1):
        print(st[i],end=" ")
    print()    