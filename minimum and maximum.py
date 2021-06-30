for i in range(int(input())):
    n=int(input())
    m=list(map(int, input().split()))
    x=min(m)
    y=len(m)
    print((y-1)*x)