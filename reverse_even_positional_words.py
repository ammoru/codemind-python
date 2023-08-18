string=input().split(" ")
lst=[]
for i in range(len(string)):
        if i%2==0:
            lst.append(string[i][::-1])
        else:
            lst.append(string[i])
            
print(*lst)            