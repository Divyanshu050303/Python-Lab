n=[]
b=[]
m=int(input("Enter the length of list"))
for i in range(m):
    n.append(int(input("Enter the next element")))
shortest = min(n)
largest=max(n)
print(shortest)
print(largest)
for j in n:
    if (j>=shortest) or (j<=largest):
        b.append(j)
        shortest=j
b.reverse()
print(b)


