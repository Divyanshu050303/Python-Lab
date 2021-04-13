for i in range(6):
    for j in range(7):
        if i==0  or (j==3 and i<6):
            print("*", end=' ')
        else:
            print(end='  ')
    print()