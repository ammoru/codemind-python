n=int(input())
k=list(map(int,input().split()))
ev= sum(k[::2])
od=sum(k[1::2])
print(abs(od-ev))