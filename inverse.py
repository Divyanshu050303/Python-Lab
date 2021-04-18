import numpy as np
m=[]
n=[]
b=[]
r=int(input("Enter the row"))
print("Enter first row")
for i in range(r):
    a=int(input("Enter the element"))
    m.append(a)
print("Enter second row")
for i in range(r):
    a=int(input("enter the element"))
    n.append(a)
print("Enter third row")
for i in range(r):
    a=int(input("Enter the element"))
    b.append(a)
M=np.array([m, n, b])
print(np.linalg.inv(M))