x =int(input("Enter first number"))
y = int(input("Enter second number"))
s=0
if x > y:
    smaller = y
else:
    smaller = x
for i in range(1, smaller+1):
    if (x % i == 0) and (y % i == 0):
        s = i
print(s)