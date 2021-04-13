for i in range(7):
    for j in range(5):
        if (j==0 and (i==0 or i==1)) or (j==4 and (i==0 or i==1)) or (i==2 and (j==1 or j==3)) or (i>2 and j==2):
            print("*", end=' ')
        else:
            print(end='  ')
    print()