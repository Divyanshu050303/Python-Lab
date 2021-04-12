for i in range(6):
    for j in range(6):
        if (i==0 and (j<6) ) or (i==1 and(j==0 or j==5)) or (i==2 and(j==0 or j==5)) or (i==3 and (j<6) ) or (i==4 and(j==0 or j==5)) or (i==5 and(j==0 or j==5)):
            print("*", end='')
        else:
            print(' ',end='')
    print()    