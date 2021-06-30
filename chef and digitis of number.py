for i in range(int(input())):
    n=input()
    a=n.count("1")
    b=n.count('0')
    if a==len(n)-1 or b==len(n)-1:
        print('Yes')
    else:
        print('No')