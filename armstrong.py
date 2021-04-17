n=int(input("Enter the number"))
b=n
m=0
while n>0:
    a = n % 10
    m=m+a**3
    n=n//10
if m==b:
    print("Number is armstrong")
else:
    print("Number is not armstrong")