def fact(n):
    if n==0:
        return 1
    return n* fact(n-1)


a=int(input("Enter the number"))
result=fact(a)
print("The factorial of a given number ", result)