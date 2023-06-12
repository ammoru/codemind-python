t=int(input())
for i in range(t):
    k=input().strip()

    if k==k[::-1]:
        if len(k)%2==0:
            print("YES EVEN")
        elif len(k)%2!=0:
            print("YES ODD")
    else:
        print("NO")