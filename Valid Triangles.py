for i in range(int(input())):
    n=input().split()
    m=int(n[0])+int(n[1])+int(n[2])
    if m==180:
        print('YES')
    else:
        print('NO')