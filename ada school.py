for i in range(int(input())):
    n, m= map(int, input().split())
    if n% 2!=0 and m% 2!=0:
        print("No")
    elif n% 2==0 and m% 2==0:
        print('Yes')
    else:
        print('Yes')