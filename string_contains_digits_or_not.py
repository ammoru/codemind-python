

def fun (mail):
    cn=0
    
    for k in mail:
        if k.isdigit():
            cn+=1
    if cn>0:
       print("Yes")
    else:
        print("No")

t=int(input())
for i in range( t):
    k=input().strip()
    fun(k)