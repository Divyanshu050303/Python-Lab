def mono(m):
    for i in range(len(m)):
        if m[i]>=m[i+1]:
            return True
        else:
            return False


n=int(input("Enter the length of array"))
m=[]
for i in range(n):
    if i not in m:
        m.append(int(input("Enter the value ")))
print(mono(m))
