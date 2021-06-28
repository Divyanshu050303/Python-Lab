for i in range(int(input())):
    a, b, c, d=map(int, input().split())
    if a==b and c==d:
        print('YES')
    elif a==c and b==d:
        print('YES')
    elif a==d and b==c:
        print('YES')
    else:
        print('NO')