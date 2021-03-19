n=input("Enter the number")
rev=0
for i in range(n):
    rem=n%10
    rev=rev*10+rem
    n=n//10
    if n==0:
        break
print(rev)
