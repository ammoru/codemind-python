lst=[]
lst2=[]
lst=input().split(" ")
for i in lst:
    lst2.append(len(i))
print(min(lst2))    