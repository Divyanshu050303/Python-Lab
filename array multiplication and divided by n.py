def arraymulti(l, m):
    mu=1
    for i in l:
        mu*=i
    k=mu%m
    print(k)


n=int(input("Enter the number of element in the array"))
m=int(input("Enter the number to divide the array multiplication"))
l=[]
for i in range(n+1):
    if i not in l:
        l.append(int(input('Enter the value')))
arraymulti(l, m)