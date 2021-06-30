for i in range(int(input())):
    n, m =map(int, input().split())
    a=list(map(int, input().split()))
    r=[]
    for j in a:
        if j<=m:
            m-=j
            r.append(1)
        else:
            r.append(0)
    print(''.join(map(str, r)))