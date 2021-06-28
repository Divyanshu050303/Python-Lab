for i in range(int(input())):
    n=list(map(int, input().split()))
    for j in range(n[0]):
        su=0
        for k in range(n[1]+1):
            su+=k
            n.remove(n[1])
            n.append(su)
    print(su)