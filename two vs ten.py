for i in range(int(input())):
    n=int(input())
    if n% 10==0:
        print('0')
    else:
        if n*2% 10==0:
            print('1')
        else:print('-1')