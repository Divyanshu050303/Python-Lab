n=input("Enter the string")
m=input("Enter the character which you want")
count=0
for i in n:
    if i==m:
        count+=1
print("The letter you want is",count)
