n=int(input())
m=n*n
st=str(m)
if st.endswith(str(n)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")