n=input()
m=int(n)**2
k=n[::-1]
n=str(int(k)**2)
if str(m)==n[::-1]:
    print(True)
else:
    print(False)