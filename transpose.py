m = []  # first matrix
n = int(input("Enter the number of rows of first matrix"))
b = int(input("Enter the number of column first matrix"))
for i in range(n):
    r = []
    for j in range(b):
        c = int(input("Enter the element "))
        r.append(c)
    m.append(r)
for i in range(n):
    for j in range(b):
        print(m[i][j], end=" ")
    print()

t = []
for i in range(n):
    d = []
    for j in range(b):
        d.append(0)
    t.append(d)
for i in range(b):
    for j in range(n):
        t[i][j] = m[j][i]
for i in range(n):
    for j in range(b):
        print(t[i][j], end=" ")
    print()