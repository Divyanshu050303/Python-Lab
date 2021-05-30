n=int(input("Enter the number of element in the array"))
m=[]
for i in range(n+1):
    if i not in m:
        m.append(int(input("Enter the value")))
s=0
for i in m:
    s+=i
print(s)