m=[]
n=int(input("Enter the number of row of first matrix"))
b=int(input("Enter the number of column of first matrix"))
for i in range(n):
    r=[]
    for j in range(b):
        s=int(input("Enter the row element "))
        r.append(s)
    m.append(r)
print(m)
m1=[]
t=int(input("Enter the number of row of first matrix"))
b=int(input("Enter the number of column of first matrix"))
for i in range(t):
    r=[]
    for j in range(b):
        s=int(input("Enter the row element "))
        r.append(s)
    m1.append(r)
print(m1)
if n==t:
    m2=[]
    for i in range(n):
        r=[]
        for j in range(b):
            z=m[i][j]+m1[i][j]
            r.append(z)
        m2.append(r)
    print(*m2, sep='\n')
else:
    print("Matrix A and B need to be the same in size")
