n=input("Enter the string")
maketrans=n.maketrans
n=n.translate(maketrans(',.', '.,'))
print(n)