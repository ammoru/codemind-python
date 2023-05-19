n=int(input())
m=n*n
ll=[]
while m>0:
    rem=m%10
    ll.append(rem) 
    m//=10
if sum(ll)==n:
    print("Neon Number")
else:
    print("Not Neon Number")