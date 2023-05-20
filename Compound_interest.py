import math
p,r,t=map(int,input().split())
l=p*((1+(r/100))**t)
print("%.2f"%l)