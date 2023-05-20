n=int(input())
k=list(map(int,input().split()))
l=len(k)//2
print(sum(k[:l]))
print(sum(k[l:len(k)]))