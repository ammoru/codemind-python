st=input()
c=0
for i in st:
    if i.isdigit():
        c+=1
if c==0:
    print("Doesn't contain digit")
else:    
    print(f"Contains {c} digit")        
        