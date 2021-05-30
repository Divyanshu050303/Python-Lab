l=list(map(int, input().split()))
c=[]
for i in range(1, len(l)+1):
    k=sum(l[0:i:1])
    if k not in c:
        c.append(k)
print(c)