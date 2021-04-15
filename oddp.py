n=input("Enter the string")
m=""
for i in range(len(n)):
    if i%2==0:
        m=m+n[i]
print(m)