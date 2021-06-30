for i in range(int(input())):
    n=int(input())
    a=list(map(int, input().split()))
    b=list(map(int, input().split()))
    c=0
    if a[0]>=b[0]:
        c=1
    for j in range(1, n):
        m=a[j]-a[j-1]
        if m>=b[j]:
            c+=1
    print(c)