for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().strip().split()))
    r = list(map(int, input().strip().split()))
    ler = list()
    for j in range(0, n):
        ler.append(l[j]*r[j])
    m = max(ler)
    c = ler.count(m)
    res = 0
    for k in range(c):
        res = max(res, r[ler.index(m)+k])
        ler.remove(m)
    print(r.index(res)+1)
