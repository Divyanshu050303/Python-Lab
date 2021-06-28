for i in range(int(input())):
    m=int(input())
    n=list(map(int, input().split()))
    k=sorted(n)
    print(k[0]+k[1])