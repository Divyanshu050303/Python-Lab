n=input("Enter the number")
m=len(n)
a=0
for i in n:
    a+=int(i)**n
if int(n)==a:
    print("Armstrong number")
else:
    print("Not a armstrong number")
    
