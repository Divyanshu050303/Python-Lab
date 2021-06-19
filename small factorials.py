for i in range(int(input())):
    n=int(input())
    f=1
    for j in range(1, n+1):
        f*=j
    print(f)