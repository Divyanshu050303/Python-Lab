for i in range(int(input())):
    l=[]
    for j in range(int(input())):
        n=list(map(int, input().split()))
        l.append(n)
    m=set(l)
    k=min(m)
    m.remove(k)
    s=0
    for k in range(int(input())):
        s+=k
    print(s)