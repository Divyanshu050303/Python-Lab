d={}
n=int(input("Enter the number"))
for i in range(1, n+1):
    m=i*i
    if i not in d:
        d.update({i: m})
print(d)