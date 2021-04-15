n=input("Enter the string")
if len(n)>2:
    if n[-3:]=="ing":
        n+="ly"
    else:
        n+="ing"
print(n)