import math
def fun(n):
    my_list=[]
    st=str(n)
    for digit in st:
        my_list.append(int(digit))
    return my_list

n=int(input())
res=fun(n)
su=sum(res)
prod=math.prod(res)

if su == prod:
    print("Spy Number")
else:
    print("Not Spy Number")