row = int(input("Enter the number of rows:"))
column = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries row wise:")
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=" ")
    print()
tran=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(row):
    for j in range(column):
        tran[i][j]=matrix[j][i]
for i in range(row):
    for j in range(column):
        print(tran[i][j], end=' ')
    print()
f=0
for i in range(row):
    for j in range(column):
        if matrix[i][j]!=tran[i][j]:
            f=1
            break
if f==0:
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")