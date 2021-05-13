m=[]  # first matrix
n=int(input("Enter the number of rows of first matrix"))
b=int(input("Enter the number of column first matrix"))
for i in range(n):
    r=[]
    for j in range(b):
        c=int(input("Enter the element "))
        r.append(c)
    m.append(r)
print(m)
w=[]  # second matrix
a=int(input("Enter the number of rows of second matrix"))
c=int(input("Enter the number of column second matrix"))
for i in range(a):
    r=[]
    for j in range(c):
        d=int(input("Enter the element "))
        r.append(d)
    w.append(r)
print(w)
if n==a:
    t=[]  # to store multiply matrix
    for i in range(n):
        C=[]
        for j in range(c):
            C.append(0)
        t.append(C)
    for i in range(0, n):
        for j in range(0, len(t[i])):
            for k in range(0, c):
                t[i][j]+=m[i][k]*w[k][j]
    for i in t:
        print(i)
else:
    print('Matrix A and B need to be the same in size')