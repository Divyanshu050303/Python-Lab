n=input("Enter the string")
m=input("Enter the string")
a=n[0:2]
b=m[0:2]
n=b+n[2:]
m=a+m[2:]
print(n, m)