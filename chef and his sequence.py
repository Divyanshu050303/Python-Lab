for i in range(int(input())):
    a=int(input())
    b=list(map(int, input().split()))
    c=int(input())
    d = list(map(int, input().split()))
    v=0
    for j in d:
        if j in b:
            v+=1
    if v==c:
        print('Yes')
    else:
        print('No')