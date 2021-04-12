for i in range(7):
    for j in range(7):
        if i==0 or i==6 or j==3:
            print("*",end='')
        else:
            print(end=' ')
    print()