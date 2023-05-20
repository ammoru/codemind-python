n=int(input())
k=list(map(int,input().split()))
l=len(k)//2
print(abs((sum(k[:l]))-(sum(k[l:len(k)]))))
