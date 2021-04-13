for i in range(7):
    for j in range(6):
        if ( i!=6 and (j==0 or j==5)) or (i==6 and (j>0 and j<5)):
            print("*", end=' ')
        else:
            print(end='  ')
    print()