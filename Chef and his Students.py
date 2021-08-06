for i in range(int(input())):
    s=input()
    a=s.count('<>')
    if a>0:
        print(a)
    else:
        print(0)