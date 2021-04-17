n=int(input("Enter the number of element in the list"))
l=[]
for i in range(n):
    m=int(input("Enter next number"))
    l.append(m)
print(l)
l.sort()
print(l)