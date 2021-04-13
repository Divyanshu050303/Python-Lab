for i in range(7):
    for j in range(7):
        if j==0 or j==6 or (i==j):
            print("*",end=' ')
        else:
            print(end='  ')
    print()