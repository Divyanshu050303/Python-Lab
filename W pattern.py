for i in range(7):
    for j in range(7):
        if j==0 or j==6 or (i==4 and j==3) or (i==5 and (j==2 or j==4)) or (i==6 and (j==1 or j==5)):
            print("*", end=' ')
        else:
            print(end='  ')
    print()