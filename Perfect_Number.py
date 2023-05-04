def perfect(l):
    su=0
    for i in range(1,l):
        if l%i==0:
            su+=i
    if su==l:
        return(True)
    else:
        return(False)

l=int(input())
print(perfect(l))

    