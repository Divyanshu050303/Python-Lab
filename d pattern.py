for i in range(7):
    for j in range(6):
        if j==0 or (i==0 and j<4) or (i==6 and j<4) or (i==1 and j==4) or (i==5 and j==4) or (j==5 and i==2) or (j==5 and i==3) or (j==5 and i==4):
            print("*",end='')
        else:
            print(end=' ')
    print()