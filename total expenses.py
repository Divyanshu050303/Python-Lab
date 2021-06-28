for i in range(int(input())):
    n, m=map(int,input().split())
    if n>1000:
        p=n*0.9*m
    else:
        p=n*m
    print("{0:.6f}".format(p))