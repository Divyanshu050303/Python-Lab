for i in range(8):
    for j in range(7):
        if (i<5 and (j==0 or j==6)) or (i==5  and (j==1 or j==5)) or (i==6 and (j==4 or j==2)) or (i==7 and j==3):
            print("*", end=' ')
        else:
            print(end='  ')
    print()