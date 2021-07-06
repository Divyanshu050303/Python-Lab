for i in range(int(input())):
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    r1 = 0
    r2 = 0
    for j in range(1, n[0]+1):
        if j in m and j in a:
            r1+=1
        elif j not in m and j not in a:
            r2+=1
    print(r1, r2)

