def reverse(num):
    res=0
    while num!=0:
        rem=num%10
        res= (res*10)+rem
        num//=10
    return res
num=int(input())
temp=num;
if (num>0):
    print(reverse(num))
else:
    print(-1*(reverse(-num)))