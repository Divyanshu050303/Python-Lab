for i in range(int(input())):
    n=int(input())
    if n<1500:
        sa=n+n*10/100+n*90/100
    else:
        sa=n+500+n*98/100
    print("{0:.2f}".format(sa))