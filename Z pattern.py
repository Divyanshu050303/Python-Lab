for  i in range(7):
    for j in range(7):
        if i==0 or i==6 or i+j==6:
            print("*", end=' ')
        else:
            print(end='  ')
    print()