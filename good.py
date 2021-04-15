n='The lyrics is not that poor!'
b='The lyrics is good!'
m=n.split()[-1]
if m=="poor!":
    n=n.replace("not that","")
else:
    b=b.replace("good!","poor!")
print(n)
print(b)
