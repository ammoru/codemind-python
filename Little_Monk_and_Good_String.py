st=input()
new_st=0
max_st=0
for k in st:
    if k in "aeiouAEIOU":
        new_st+=1
        if new_st>max_st:
            max_st=new_st
    else:
        new_st=0
print(max_st)        
        
        