for i in range(int(input())):
    a=int(input())
    n=list(map(int, input().split()))
    m=list(map(int, input().split()))
    l=[]
    for j in range(a):
        s=n[j]*20-m[j]*10
        l.append(s)
    print(max(l))
