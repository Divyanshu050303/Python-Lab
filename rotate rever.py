def rotate(m, n,  p):
    tem=[]
    for i in range(0, p):
        if m[i] not in tem:
            tem.append(m[i])
    i=0
    while p<n:
        m[i]=m[p]
        i+=1
        p+=1
    m[:]=m[:i]+tem
    return m
def reverse(m)

n=int(input("Enter the number of element of the array"))
m=[]
p=int(input("Enter the position"))
for i in range(n+1):
    if i not in m:
        m.append(int(input("Enter the value")))
print(rotate(m, len(m), p))
