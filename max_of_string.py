n=input()
new=[]
for i in n:
    new.append(ord(i))
print(chr(max(new)))