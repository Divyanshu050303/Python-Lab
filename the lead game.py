l=[]
for i in range(int(input())):
    n=input().split()
    m=int(n[0])-int(n[1])
    l.append(abs(m))
print(max(l))